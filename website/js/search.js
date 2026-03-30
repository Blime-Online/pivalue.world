/**
 * Pi Value World - Search Functionality
 */

document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchQuery = document.getElementById('searchQuery');
    const searchResults = document.getElementById('searchResults');
    const submissionDetail = document.getElementById('submissionDetail');
    const recentList = document.getElementById('recentList');
    
    // Handle search form submission
    if (searchForm) {
        searchForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const query = searchQuery.value.trim();
            
            if (!query) {
                showStatusMessage('Please enter a search query', 'error');
                return;
            }
            
            await performSearch(query);
        });
    }
    
    // Load recent submissions
    loadRecentSubmissions();
    
    // Close detail view
    const closeDetail = document.getElementById('closeDetail');
    if (closeDetail) {
        closeDetail.addEventListener('click', () => {
            submissionDetail.style.display = 'none';
        });
    }
    
    // Copy link button
    const copyLinkBtn = document.getElementById('copyLinkBtn');
    if (copyLinkBtn) {
        copyLinkBtn.addEventListener('click', () => {
            const url = window.location.href.split('?')[0];
            const currentId = document.getElementById('detailId')?.textContent;
            
            if (currentId) {
                const shareUrl = `${url}?id=${currentId}`;
                navigator.clipboard.writeText(shareUrl).then(() => {
                    showStatusMessage('Link copied to clipboard!', 'success');
                }).catch(() => {
                    showStatusMessage('Failed to copy link', 'error');
                });
            }
        });
    }
});

async function performSearch(query) {
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '<p class="loading">Searching...</p>';
    
    try {
        const result = await window.PiValueDB.searchSubmission(query);
        
        if (result.success && result.data) {
            displaySubmission(result.data);
        } else if (result.error && result.error.includes('not found')) {
            resultsDiv.innerHTML = `
                <div class="no-results">
                    <h3>No Results Found</h3>
                    <p>We couldn't find a submission with that ID or code.</p>
                    <p>Make sure you entered the correct Submission ID or Verification Code.</p>
                </div>
            `;
        } else {
            throw new Error(result.error || 'Search failed');
        }
    } catch (error) {
        console.error('Search error:', error);
        resultsDiv.innerHTML = `
            <div class="error-message">
                <h3>Search Error</h3>
                <p>An error occurred while searching. Please try again.</p>
                <p><small>${error.message}</small></p>
            </div>
        `;
    }
}

function displaySubmission(submission) {
    const detailView = document.getElementById('submissionDetail');
    if (!detailView) return;
    
    // Fill in the details
    document.getElementById('detailStatus').textContent = 
        submission.status ? submission.status.charAt(0).toUpperCase() + submission.status.slice(1) : 'Unknown';
    document.getElementById('detailStatus').className = 
        `status-badge ${submission.status || 'pending'}`;
    
    document.getElementById('detailUsername').textContent = submission.github_username || 'N/A';
    document.getElementById('detailTimeLimit').textContent = `${submission.time_limit || 0} minute(s)`;
    document.getElementById('detailCalculations').textContent = 
        formatNumber(submission.calculations_performed || 0);
    document.getElementById('detailPrecision').textContent = 
        `${submission.precision_digits || 0} decimal places`;
    
    const submittedDate = submission.submitted_at || submission.created_at;
    document.getElementById('detailSubmitted').textContent = submittedDate ? 
        formatDate(submittedDate) : 'N/A';
    
    document.getElementById('detailCode').textContent = submission.verification_code || 'N/A';
    document.getElementById('detailId').textContent = submission.submission_id || 'N/A';
    
    // Show generate certificate button if verified
    const generateCertBtn = document.getElementById('generateCertBtn');
    if (generateCertBtn) {
        if (submission.status === 'verified') {
            generateCertBtn.style.display = 'inline-block';
            generateCertBtn.onclick = () => generateCertificate(submission);
        } else {
            generateCertBtn.style.display = 'none';
        }
    }
    
    // Show the detail view
    detailView.style.display = 'block';
    detailView.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function loadRecentSubmissions() {
    const recentList = document.getElementById('recentList');
    if (!recentList) return;
    
    try {
        const result = await window.PiValueDB.getRecentSubmissions(5);
        
        if (result.success && result.data && result.data.length > 0) {
            displayRecentSubmissions(result.data);
        } else {
            recentList.innerHTML = '<p class="loading">No recent submissions yet. Be the first!</p>';
        }
    } catch (error) {
        console.error('Error loading recent submissions:', error);
        recentList.innerHTML = '<p class="loading">Unable to load recent submissions</p>';
    }
}

function displayRecentSubmissions(submissions) {
    const recentList = document.getElementById('recentList');
    if (!recentList) return;
    
    const html = submissions.map(sub => `
        <div class="recent-item" onclick="showRecentDetail('${sub.submission_id}')">
            <div class="recent-item-header">
                <span class="recent-username">${escapeHtml(sub.github_username)}</span>
                <span class="status-badge ${sub.status || 'pending'}">
                    ${sub.status ? sub.status.charAt(0).toUpperCase() + sub.status.slice(1) : 'Pending'}
                </span>
            </div>
            <div class="recent-item-details">
                <span>⏱️ ${sub.time_limit || 0} min</span>
                <span>🔢 ${formatNumber(sub.calculations_performed || 0)} calcs</span>
                <span>📊 ${sub.precision_digits || 0} digits</span>
            </div>
        </div>
    `).join('');
    
    recentList.innerHTML = html;
}

function showRecentDetail(submissionId) {
    document.getElementById('searchQuery').value = submissionId;
    performSearch(submissionId);
}

function generateCertificate(submission) {
    // Redirect to certificate page with submission data
    const certUrl = `certificate.html?id=${submission.submission_id}`;
    window.location.href = certUrl;
}

// Helper functions
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showStatusMessage(message, type = 'info') {
    // Create status message if it doesn't exist
    let statusDiv = document.getElementById('statusMessage');
    if (!statusDiv) {
        statusDiv = document.createElement('div');
        statusDiv.id = 'statusMessage';
        statusDiv.className = 'status-message';
        document.querySelector('.search-container')?.after(statusDiv);
    }
    
    statusDiv.textContent = message;
    statusDiv.className = `status-message ${type}`;
    statusDiv.style.display = 'block';
    
    setTimeout(() => {
        statusDiv.style.display = 'none';
    }, 5000);
}
