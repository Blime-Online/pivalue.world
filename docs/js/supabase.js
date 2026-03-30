/**
 * Pi Value World - Supabase Configuration
 * 
 * IMPORTANT: Replace these values with your actual Supabase credentials
 * 
 * Setup Instructions:
 * 1. Go to https://supabase.com and create a new project
 * 2. Get your project URL and anon key from Settings > API
 * 3. Replace the values below
 * 4. Create the database tables using the SQL schema provided
 */

// Supabase Configuration
const SUPABASE_CONFIG = {
    url: (window.PiValueWebConfig && window.PiValueWebConfig.SUPABASE_URL) || 'https://ywpjpzbembudsyihxylz.supabase.co',
    anonKey: (window.PiValueWebConfig && window.PiValueWebConfig.SUPABASE_ANON_KEY) || 'sb_publishable_ikmQddB_jRs42qrkHBL6tg_f65ek8YU'
};

// Initialize Supabase client
let supabaseClient = null;

function getSupabaseClient() {
    if (!supabaseClient) {
        if (SUPABASE_CONFIG.url === 'YOUR_SUPABASE_URL' || !SUPABASE_CONFIG.url) {
            console.warn('⚠️ Supabase not configured! Using mock mode.');
            console.warn('Follow setup instructions in js/supabase.js to configure.');
            return createMockSupabaseClient();
        }
        
        // Initialize with actual Supabase client
        supabaseClient = window.supabase.createClient(
            SUPABASE_CONFIG.url,
            SUPABASE_CONFIG.anonKey
        );
    }
    return supabaseClient;
}

// Mock client for development without Supabase
function createMockSupabaseClient() {
    console.log('🔧 Using mock Supabase client for development');
    
    return {
        from: function(table) {
            return {
                select: async function(columns = '*') {
                    console.log(`[MOCK] SELECT ${columns} FROM ${table}`);
                    return { data: [], error: null };
                },
                insert: async function(data) {
                    console.log(`[MOCK] INSERT INTO ${table}`, data);
                    return { data: { id: 'mock_' + Date.now() }, error: null };
                },
                update: async function(data) {
                    console.log(`[MOCK] UPDATE ${table}`, data);
                    return { data: null, error: null };
                },
                eq: async function(column, value) {
                    console.log(`[MOCK] WHERE ${column} = ${value}`);
                    return { data: null, error: null };
                }
            };
        },
        rpc: async function(functionName, params) {
            console.log(`[MOCK] RPC ${functionName}`, params);
            return { data: 3.14, error: null };
        }
    };
}

// Database Operations
async function submitCalculation(submissionData) {
    /**
     * Submit a new calculation result
     * 
     * submissionData: {
     *   github_username: string,
     *   verification_code: string,
     *   submission_id: string,
     *   time_limit: number,
     *   calculations_performed: number,
     *   precision_digits: number,
     *   elapsed_seconds: number,
     *   status: 'pending' | 'verified' | 'rejected'
     * }
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('submissions')
            .insert([submissionData]);
        
        if (error) throw error;
        return { success: true, data };
    } catch (error) {
        console.error('Error submitting calculation:', error);
        return { success: false, error: error.message };
    }
}

async function searchSubmission(query) {
    /**
     * Search for a submission by ID or verification code
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('submissions')
            .select('*')
            .or(`submission_id.eq.${query},verification_code.eq.${query}`)
            .single();
        
        if (error && error.code !== 'PGRST116') throw error; // PGRST116 = not found
        return { success: true, data };
    } catch (error) {
        console.error('Error searching submission:', error);
        return { success: false, error: error.message };
    }
}

async function getRecentSubmissions(limit = 10) {
    /**
     * Get recent submissions
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('submissions')
            .select('*')
            .order('created_at', { ascending: false })
            .limit(limit);
        
        if (error) throw error;
        return { success: true, data };
    } catch (error) {
        console.error('Error getting recent submissions:', error);
        return { success: false, error: error.message };
    }
}

async function verifySubmission(code) {
    /**
     * Verify a submission by verification code
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('submissions')
            .select('*')
            .eq('verification_code', code)
            .eq('status', 'verified')
            .single();
        
        if (error && error.code !== 'PGRST116') throw error;
        return { success: true, data, verified: !!data };
    } catch (error) {
        console.error('Error verifying submission:', error);
        return { success: false, error: error.message, verified: false };
    }
}

async function incrementPiCounterBy(count = 1) {
    let success = true;
    for (let i = 0; i < count; i += 1) {
        const result = await incrementPiCounter();
        if (!result.success) {
            success = false;
            break;
        }
    }
    return { success };
}

async function upsertSubmissionFromRepo(record) {
    /**
     * Upsert a submission that exists in the GitHub verification list.
     * If the submission is new or pending, mark it verified and increment Pi counter.
     */
    try {
        const supabase = getSupabaseClient();

        // Check existing record by submission_id
        const existing = await supabase
            .from('submissions')
            .select('*')
            .eq('submission_id', record.submission_id)
            .single();

        if (existing.error && existing.error.code !== 'PGRST116') {
            throw existing.error;
        }

        if (!existing.data) {
            // New submission: insert directly as verified
            const insertPayload = {
                ...record,
                status: 'verified',
                verified_at: new Date().toISOString(),
                created_at: record.created_at || new Date().toISOString(),
                submitted_at: record.submitted_at || new Date().toISOString()
            };

            const { error: insertError } = await supabase
                .from('submissions')
                .insert([insertPayload]);

            if (insertError) throw insertError;

            // Generate certificate record if not existing
            await createCertificate({
                submission_id: record.submission_id,
                certificate_url: `https://pivalue.iths.online/certificate.html?id=${record.submission_id}`,
                certificate_data: insertPayload
            });

            return { status: 'inserted', verified: true };
        }

        if (existing.data.status !== 'verified') {
            const { error: updateError } = await supabase
                .from('submissions')
                .update({ status: 'verified', verified_at: new Date().toISOString() })
                .eq('submission_id', record.submission_id);

            if (updateError) throw updateError;

            // Ensure certificate record exists
            await createCertificate({
                submission_id: record.submission_id,
                certificate_url: `https://pivalue.iths.online/certificate.html?id=${record.submission_id}`,
                certificate_data: { ...existing.data, status: 'verified' }
            });

            return { status: 'updated', verified: true };
        }

        return { status: 'already_verified', verified: false };
    } catch (error) {
        console.error('Error upserting repo submission:', error);
        return { success: false, error: error.message };
    }
}

async function syncVerificationListFromGitHub(config = {}) {
    /**
     * Sync submissions from GitHub verification_list folder and auto-verify
     * config: { owner, repo, path, token }
     */
    try {
        const { owner, repo, path, token } = config;
        if (!owner || !repo || !path) {
            throw new Error('GitHub sync config is incomplete');
        }

        const apiUrl = `https://api.github.com/repos/${owner}/${repo}/contents/${path}`;
        const headers = {
            Accept: 'application/vnd.github+json'
        };
        if (token) {
            headers.Authorization = `Bearer ${token}`;
        }

        const listResponse = await fetch(apiUrl, { headers });
        if (!listResponse.ok) {
            throw new Error(`GitHub list fetch failed: ${listResponse.status}`);
        }

        const files = await listResponse.json();
        if (!Array.isArray(files)) {
            throw new Error('GitHub verification list directory not found or empty');
        }

        let newlyVerifiedCount = 0;

        for (const file of files) {
            if (!file.name.endsWith('.json') || file.type !== 'file') continue;

            const contentResponse = await fetch(file.download_url, { headers });
            if (!contentResponse.ok) continue;

            const text = await contentResponse.text();
            let payload;
            try {
                payload = JSON.parse(text);
            } catch (err) {
                console.warn(`Skipping invalid JSON file ${file.name}`);
                continue;
            }

            if (!payload.submission_id || !payload.verification_code) {
                console.warn(`Skipping incomplete submission data in ${file.name}`);
                continue;
            }

            const upsertResult = await upsertSubmissionFromRepo(payload);
            if (upsertResult.verified) {
                newlyVerifiedCount += 1;
            }
        }

        if (newlyVerifiedCount > 0) {
            // Increment global Pi counter by 0.01 for each new verified item
            const incResult = await incrementPiCounterBy(newlyVerifiedCount);
            if (!incResult.success) {
                console.warn('Failed to increment Pi counter for all verified submissions');
            }
        }

        return { success: true, newlyVerifiedCount };
    } catch (error) {
        console.error('Error syncing verification list from GitHub:', error);
        return { success: false, error: error.message };
    }
}

async function getPiCounter() {
    /**
     * Get the current Pi counter value
     * This increments with each successful merge
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('counter')
            .select('value')
            .single();
        
        if (error) {
            if (error.code === 'PGRST116') {
                // No counter yet, return default
                return 3.14;
            }
            throw error;
        }
        
        return data ? data.value : 3.14;
    } catch (error) {
        console.error('Error getting Pi counter:', error);
        return 3.14;
    }
}

async function incrementPiCounter() {
    /**
     * Increment the Pi counter (called on successful merge)
     */
    try {
        const supabase = getSupabaseClient();
        
        // Get current value
        const currentValue = await getPiCounter();
        const newValue = currentValue + 0.01;
        
        // Update or insert
        const { data, error } = await supabase
            .from('counter')
            .upsert({ id: 1, value: parseFloat(newValue.toFixed(2)) });
        
        if (error) throw error;
        return { success: true, value: newValue };
    } catch (error) {
        console.error('Error incrementing counter:', error);
        return { success: false, error: error.message };
    }
}

async function createCertificate(certData) {
    /**
     * Create a certificate record
     * 
     * certData: {
     *   submission_id: string,
     *   certificate_url: string,
     *   certificate_data: object
     * }
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('certificates')
            .insert([certData]);
        
        if (error) throw error;
        return { success: true, data };
    } catch (error) {
        console.error('Error creating certificate:', error);
        return { success: false, error: error.message };
    }
}

async function getCertificate(submissionId) {
    /**
     * Get certificate by submission ID
     */
    try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
            .from('certificates')
            .select('*')
            .eq('submission_id', submissionId)
            .single();
        
        if (error && error.code !== 'PGRST116') throw error;
        return { success: true, data };
    } catch (error) {
        console.error('Error getting certificate:', error);
        return { success: false, error: error.message };
    }
}

// Export functions
window.PiValueDB = {
    submitCalculation,
    searchSubmission,
    getRecentSubmissions,
    verifySubmission,
    syncVerificationListFromGitHub,
    upsertSubmissionFromRepo,
    getPiCounter,
    incrementPiCounter,
    incrementPiCounterBy,
    createCertificate,
    getCertificate,
    getSupabaseClient
};

// Auto-initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('🥧 Pi Value World - Database Module Loaded');
    
    // Check if Supabase script is loaded
    if (!window.supabase) {
        console.warn('⚠️ Supabase JS library not loaded!');
        console.warn('Add this to your HTML:');
        console.warn('<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>');
    }
});
