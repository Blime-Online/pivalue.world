/*
 * Pi Value World - Client Configuration
 *
 * For security, do not commit sensitive values to source control.
 * Use CI or deployment process to inject environment-specific values.
 */

window.PiValueWebConfig = {
    // GitHub token used by the browser sync function (optional; if set, use a read-only PAT).
    // In production, this should be read-only token with minimal permissions.
    GITHUB_SYNC_TOKEN: '',

    // Supabase values may also be set here; these are used by the client when available.
    SUPABASE_URL: '',
    SUPABASE_ANON_KEY: ''
};
