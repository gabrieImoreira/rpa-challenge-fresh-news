btn_search = 'xpath://button[@data-element="search-button"]'
input_search = 'xpath://input[@data-element="search-form-input"]'
select_sort_by = 'xpath://select[@class="select-input"]'
btn_submit_search = 'xpath://button[@data-element="search-submit-button"]'
input_topic = 'xpath://span[contains(text(),"{topic}")]/parent::label/input[@class="checkbox-input-element"]'
menu_tab = 'xpath://div[@class="search-results-module-ajax"]'
menu_no_results = 'xpath://*[contains(text(),"There are not any results that match")]'
menu_search_results = 'xpath://ul[@class="search-results-module-results-menu"]/li'
menu_search_results_title = 'xpath:(//h3[@class="promo-title"])[{count}]'
menu_search_results_description = 'xpath:(//p[@class="promo-description"])[{count}]'
menu_search_results_timestamp = 'xpath:(//p[@class="promo-timestamp"])[{count}]'
menu_search_results_img= 'xpath:(//img[@class="image"])[{count}]'
label_page_counts =  'xpath://div[@class="search-results-module-page-counts"]'
btn_next_page = 'xpath://div[@class="search-results-module-next-page"]/a'