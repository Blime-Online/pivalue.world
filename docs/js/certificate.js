/**
 * Pi Value World - Certificate Generation and Management
 * Generates certificates with username, time limit, calculations, precision,
 * verification code, submission ID, and Pi Value World logo
 */

let currentSubmission = null;

document.addEventListener('DOMContentLoaded', async () => {
    // Check if we have an ID in the URL
    const urlParams = new URLSearchParams(window.location.search);
    const submissionId = urlParams.get('id');
    
    if (submissionId) {
        await loadCertificate(submissionId);
    } else {
        showPlaceholder();
    }
    
    // Setup button handlers
    setupButtons();
});

async function loadCertificate(submissionId) {
    try {
        const result = await window.PiValueDB.searchSubmission(submissionId);
        
        if (result.success && result.data) {
            if (result.data.status === 'verified') {
                displayCertificate(result.data);
            } else {
                showNotVerifiedMessage(result.data.status);
            }
        } else {
            showNotFoundMessage();
        }
    } catch (error) {
        console.error('Error loading certificate:', error);
        showErrorState();
    }
}

function displayCertificate(submission) {
    currentSubmission = submission;
    
    // Fill in certificate data
    document.getElementById('certUsername').textContent = `@${submission.github_username}`;
    document.getElementById('certTimeLimit').textContent = `${submission.time_limit} minute(s)`;
    document.getElementById('certCalculations').textContent = formatNumber(submission.calculations_performed);
    document.getElementById('certPrecision').textContent = `${submission.precision_digits} decimal places`;
    document.getElementById('certCode').textContent = submission.verification_code;
    document.getElementById('certId').textContent = submission.submission_id;
    
    const submittedDate = submission.submitted_at || submission.created_at;
    document.getElementById('certDate').textContent = formatDate(submittedDate);
    
    // Show the certificate
    document.getElementById('certificateContainer').style.opacity = '1';
}

function showPlaceholder() {
    const container = document.getElementById('certificateContainer');
    container.innerHTML = `
        <div class="placeholder-message">
            <h2>🎓 Certificate Preview</h2>
            <p>This is a preview of what your certificate will look like.</p>
            <p>To generate your certificate:</p>
            <ol style="text-align: left; max-width: 500px; margin: 2rem auto;">
                <li>Run the calculation script</li>
                <li>Submit your results for verification</li>
                <li>Wait for maintainer approval</li>
                <li>Once verified, you'll receive a link to your certificate</li>
            </ol>
            <a href="README.md" class="btn btn-primary btn-large" style="margin-top: 2rem;">
                Submit Your Results via PR instructions
            </a>
        </div>
    `;
    
    // Hide action buttons
    document.querySelector('.certificate-actions').style.display = 'none';
    document.querySelector('.sharing-options').style.display = 'none';
}

function showNotVerifiedMessage(status) {
    const container = document.getElementById('certificateContainer');
    const statusText = status ? status.charAt(0).toUpperCase() + status.slice(1) : 'Pending';
    
    container.innerHTML = `
        <div class="not-verified-message">
            <h2>⏳ Certificate Not Ready</h2>
            <p>This submission is currently <strong>${statusText}</strong>.</p>
            <p>Certificates are only available for verified submissions.</p>
            <div style="margin-top: 2rem;">
                <a href="search.html?id=${currentSubmission?.submission_id}" class="btn btn-secondary">
                    View Submission Status
                </a>
            </div>
        </div>
    `;
    
    document.querySelector('.certificate-actions').style.display = 'none';
    document.querySelector('.sharing-options').style.display = 'none';
}

function showNotFoundMessage() {
    const container = document.getElementById('certificateContainer');
    container.innerHTML = `
        <div class="not-found-message">
            <h2>❌ Submission Not Found</h2>
            <p>We couldn't find a submission with that ID.</p>
            <p>Please check your link and try again.</p>
            <div style="margin-top: 2rem;">
                <a href="search.html" class="btn btn-primary">Search Submissions</a>
            </div>
        </div>
    `;
    
    document.querySelector('.certificate-actions').style.display = 'none';
    document.querySelector('.sharing-options').style.display = 'none';
}

function showErrorState() {
    const container = document.getElementById('certificateContainer');
    container.innerHTML = `
        <div class="error-message">
            <h2>⚠️ Error Loading Certificate</h2>
            <p>An error occurred while loading the certificate.</p>
            <p>Please try again later or contact support.</p>
            <div style="margin-top: 2rem;">
                <a href="index.html" class="btn btn-primary">Go Home</a>
            </div>
        </div>
    `;
    
    document.querySelector('.certificate-actions').style.display = 'none';
    document.querySelector('.sharing-options').style.display = 'none';
}

function setupButtons() {
    // Download PNG
    const downloadPngBtn = document.getElementById('downloadPngBtn');
    if (downloadPngBtn) {
        downloadPngBtn.addEventListener('click', downloadAsPNG);
    }
    
    // Download PDF
    const downloadPdfBtn = document.getElementById('downloadPdfBtn');
    if (downloadPdfBtn) {
        downloadPdfBtn.addEventListener('click', downloadAsPDF);
    }
    
    // Share Link
    const shareLinkBtn = document.getElementById('shareLinkBtn');
    if (shareLinkBtn) {
        shareLinkBtn.addEventListener('click', copyShareableLink);
    }
    
    // Social Share Buttons
    setupSocialShare();
}

async function downloadAsPNG() {
    if (!currentSubmission) return;
    
    try {
        const element = document.getElementById('certificateContainer');
        
        const canvas = await window.html2canvas(element, {
            scale: 2,
            useCORS: true,
            backgroundColor: '#ffffff'
        });
        
        canvas.toBlob((blob) => {
            if (blob) {
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.download = `pi_certificate_${currentSubmission.github_username}.png`;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(url);
                
                showStatusMessage('Certificate downloaded as PNG!', 'success');
            }
        }, 'image/png');
    } catch (error) {
        console.error('Error downloading PNG:', error);
        showStatusMessage('Failed to download certificate', 'error');
    }
}

async function downloadAsPDF() {
    if (!currentSubmission) return;
    
    try {
        const { jsPDF } = window.jspdf;
        const element = document.getElementById('certificateContainer');
        
        const canvas = await window.html2canvas(element, {
            scale: 2,
            useCORS: true,
            backgroundColor: '#ffffff'
        });
        
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jsPDF({
            orientation: 'landscape',
            unit: 'mm',
            format: 'a4'
        });
        
        const imgWidth = 297; // A4 landscape width in mm
        const pageHeight = 210; // A4 landscape height in mm
        const imgHeight = (canvas.height * imgWidth) / canvas.width;
        const marginTop = (pageHeight - imgHeight) / 2;
        
        pdf.addImage(imgData, 'PNG', 0, marginTop, imgWidth, imgHeight);
        pdf.save(`pi_certificate_${currentSubmission.github_username}.pdf`);
        
        showStatusMessage('Certificate downloaded as PDF!', 'success');
    } catch (error) {
        console.error('Error downloading PDF:', error);
        showStatusMessage('Failed to download PDF', 'error');
    }
}

function copyShareableLink() {
    if (!currentSubmission) return;
    
    const baseUrl = window.location.href.split('?')[0];
    const shareUrl = `${baseUrl}?id=${currentSubmission.submission_id}`;
    
    navigator.clipboard.writeText(shareUrl).then(() => {
        showStatusMessage('Link copied to clipboard!', 'success');
    }).catch(() => {
        showStatusMessage('Failed to copy link', 'error');
    });
}

function setupSocialShare() {
    if (!currentSubmission) return;
    
    const shareUrl = encodeURIComponent(`${window.location.origin}/certificate.html?id=${currentSubmission.submission_id}`);
    const text = encodeURIComponent(`I just earned a Pi Certificate on Pi Value World! Check out my achievement: ${currentSubmission.github_username} calculated 22/7 ${formatNumber(currentSubmission.calculations_performed)} times in ${currentSubmission.time_limit} minutes!`);
    
    // GitHub
    const githubBtn = document.getElementById('shareGithub');
    if (githubBtn) {
        githubBtn.href = 'https://github.com/harinandsindukumar/pivalue.world';
        githubBtn.title = 'Add to your GitHub profile README';
    }
    
    // Twitter
    const twitterBtn = document.getElementById('shareTwitter');
    if (twitterBtn) {
        twitterBtn.href = `https://twitter.com/intent/tweet?text=${text}&url=${shareUrl}`;
    }
    
    // LinkedIn
    const linkedinBtn = document.getElementById('shareLinkedIn');
    if (linkedinBtn) {
        linkedinBtn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${shareUrl}`;
    }
}

function showStatusMessage(message, type = 'info') {
    // Create or get status message element
    let statusDiv = document.getElementById('certStatusMessage');
    if (!statusDiv) {
        statusDiv = document.createElement('div');
        statusDiv.id = 'certStatusMessage';
        statusDiv.className = 'status-message';
        document.querySelector('.certificate-actions')?.before(statusDiv);
    }
    
    statusDiv.textContent = message;
    statusDiv.className = `status-message ${type}`;
    statusDiv.style.display = 'block';
    
    setTimeout(() => {
        statusDiv.style.display = 'none';
    }, 5000);
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
