FROM frappe/erpnext:v15
RUN bench get-app dfp_external_storage --branch version-15 https://github.com/developmentforpeople/dfp_external_storage; bench setup requirements dfp_external_storage;
RUN echo "version: 2023.11.23 0738"; bench get-app site_cm --branch version-15 https://github.com/developmentforpeople/site_cm; bench setup requirements site_cm;