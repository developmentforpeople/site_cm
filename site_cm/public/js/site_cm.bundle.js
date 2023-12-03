
console.log('js bundle loaded!')

frappe.ready(() => {
	frappe.setup_search('#search-box-body', '')
	frappe.setup_search('#search-box-header', '')
})
