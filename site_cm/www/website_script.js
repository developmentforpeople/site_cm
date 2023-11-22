// website_script.js
{% if javascript -%}{{ javascript }}{%- endif %}

{% if google_analytics_id -%}
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', '{{ google_analytics_id }}', 'auto');
{% if google_analytics_anonymize_ip %}
ga('set', 'anonymizeIp', true);
{% endif %}
ga('send', 'pageview');
// End Google Analytics
{%- endif %}

{% if enable_view_tracking %}
if (navigator.doNotTrack != 1 && !window.is_404) {
	function generateBrowserHash() {
		const navigatorData = [
			navigator.userAgent,
			// navigator.language,
			navigator.platform,
			navigator.hardwareConcurrency,
			screen.colorDepth,
			screen.pixelDepth,
			screen.width,
			screen.height,
			navigator.deviceMemory,
			navigator.maxTouchPoints,
			navigator.vendor,
		].join('');
		return crypto.subtle.digest('SHA-256', new TextEncoder().encode(navigatorData))
			.then(hash => {
				let hexString = '';
				const hashBuffer = new Uint8Array(hash);
				hashBuffer.forEach(b => {
					hexString += b.toString(16).padStart(2, '0');
				});
				return hexString;
			});
	}
	frappe.ready(() => {
		let browser = frappe.utils.get_browser();
		let query_params = frappe.utils.get_query_params();
		generateBrowserHash().then(hash => {
			frappe.call("frappe.website.doctype.web_page_view.web_page_view.make_view_log", {
				referrer: document.referrer,
				browser: browser.name,
				version: browser.version,
				user_tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
				source: query_params.source,
				medium: query_params.medium,
				campaign: query_params.campaign,
				visitor_id: hash,
			})
		})
	})
}
{% endif %}