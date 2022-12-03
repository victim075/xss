import requests

# Set the base URL for the API
base_url = "https://dash.cloudflare.com/api/v4/accounts/fa8066bb9f6de3e92eaff76ec6ec9856/email/routing/addresses"

# Set the headers for the GET request
get_headers = {
    "Host": "dash.cloudflare.com",
    "Cookie": "sparrow_id=%7B%22deviceId%22%3A%22c8c29006-ab33-4abd-9a17-516d536e2835%22%2C%22userId%22%3A%22b7b1ad6d2cb38e1bc85ef9095c91cabb%22%7D; __stripe_mid=9066d3ec-ee7a-4f79-b1db-585640bd1f7db2ae64; __cf_logged_in=1; CF_VERIFIED_DEVICE_26dd4b974d6427f20806e4a9a331624a8606b8a2422c0acfe2f1e25cfb261979=1669794678; CF_VERIFIED_DEVICE_14f5e40d61fc9ef2a87e78bcc5b0a7d4992fd3a4b091ba1cd1cfbd9c9e512ef8=1669825129; _ga=GA1.2.1889906617.1669825197; oauth2_authentication_csrf_insecure=MTY2OTgzMzkzN3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRE5pWlRGak5tWmtNVE0yTnpReVltWmlNalUzTjJJM01tSTBOMlF3TURFenxeV52m-EolTgLTBPf9w0qf2FP57MKSHiSFvT3ZiPBP1w==; oauth2_consent_csrf_insecure=MTY2OTgzMzk0OXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRGRqWm1JeU1qbGtOV0ZoTXpSbU5XRTVZakprTlRJNE5tRmxaVGRsWkRreXzumh3rmhcv749UQNjGHpc-oPE7Y2kzIsQO9RH2bvHjCw==; _gcl_au=1.1.907927322.1669825478; _ga_PHVG60J2FD=GS1.1.1670002561.4.1.1670004585.60.0.0; _mkto_trk=id:713-XSC-918&token:_mch-cloudflare.com-1669825480480-69396; CF_VERIFIED_DEVICE_274167e18b9d18496059b5b36620e515a2d0a60fb2133023e89b85064d60c7eb=1670001892; cf_clearance=GNzGE5BUpfdl8JIyQl2ZUKlEst3nJT2.R_0ynZysf78-1669831781-0-250; _fbp=fb.2.1669835157741.1710303466; _rdt_uuid=1669835157741.e4b7d313-0fdb-4c47-83ab-4d693332e600; cfmrk_cic={"id":"tZDL9AQSa2il4ioaWODMaBpgsD5bOSnv","v1":0,"v2":0,"v3":0,"v5":0,"v7":0,"v8":0,"v6":0}; gates_cohorts=%7B%7D; CF_checkout={%227223234da8c2d1f0980f037c798387f0%22:{%22items%22:[{%22key%22:%22r2_basic%22}]}%2C%22fa8066bb9f6de3e92eaff76ec6ec9856%22:{%22items%22:[]%2C%22next%22:{%22path%22:%22/fa8066bb9f6de3e92eaff76ec6ec9856/stream%22%2C%22label%22:%22Return%20to%20Cloudflare%20Stream%22}}}; _gid=GA1.2.1733856312.1669989428; __cf_effload=1; CF_VERIFIED_DEVICE_f3efb117f44720e070094369989a5c61c3834dc123fb905940f2c92bfb692423=1670000516; vses2=b7b1ad6d2c-3kk46tqqpsqu4jldrp96ohd2bh8jk6p3; __cflb=0H28upHR6WxXGRqfrsmcyJP33mXipsFZndZRhGtCxQD; __cf_bm=WpvAExdWIFkwfo6k839GWlFori91X373iHX2OSQEuJI-1670051252-0-AR9PErqMtqub7qifUVbzGU8NvZvIwj5Qm/7WdPQvJt3xXn0lRWQOKBjDs+GIVbE8SJRO5PpcwlOv359q8SocSR8WxOKRHKfCcWCYtie5sXB6; __stripe_sid=7e9fc816-6a35-4e25-84b4-2123a4499a27840d6f",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://dash.cloudflare.com/",
    "X-Atok": "1670094193-ATOK39a339c01d919ad5df04e808263088b993de993143256e38",
    "X-Cross-Site-Security": "dash",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}

# Make the GET request to fetch the tag value
response = requests.get(base_url, headers=get_headers)

# Extract the tag value from the response
tag_value = response.json()["tag"]

# Set the headers for the DELETE request
delete_headers = {
    "Host": "dash.cloudflare.com",
    "Cookie": "sparrow_id=%7B%22deviceId%22%3A%22c8c29006-ab33-4abd-9a17-516d536e2835%22%2C%22userId%22%3A%22b7b1ad6d2cb38e1bc85ef9095c91cabb%22%7D; __stripe_mid=9066d3ec-ee7a-4f79-b1db-585640bd1f7db2ae64; __cf_logged_in=1; CF_VERIFIED_DEVICE_26dd4b974d6427f20806e4a9a331624a8606b8a2422c0acfe2f1e25cfb261979=1669794678; CF_VERIFIED_DEVICE_14f5e40d61fc9ef2a87e78bcc5b0a7d4992fd3a4b091ba1cd1cfbd9c9e512ef8=1669825129; _ga=GA1.2.1889906617.1669825197; oauth2_authentication_csrf_insecure=MTY2OTgzMzkzN3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRE5pWlRGak5tWmtNVE0yTnpReVltWmlNalUzTjJJM01tSTBOMlF3TURFenxeV52m-EolTgLTBPf9w0qf2FP57MKSHiSFvT3ZiPBP1w==; oauth2_consent_csrf_insecure=MTY2OTgzMzk0OXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRGRqWm1JeU1qbGtOV0ZoTXpSbU5XRTVZakprTlRJNE5tRmxaVGRsWkRreXzumh3rmhcv749UQNjGHpc-oPE7Y2kzIsQO9RH2bvHjCw==; _gcl_au=1.1.907927322.1669825478; _ga_PHVG60J2FD=GS1.1.1670002561.4.1.1670004585.60.0.0; _mkto_trk=id:713-XSC-918&token:_mch-cloudflare.com-1669825480480-69396; CF_VERIFIED_DEVICE_274167e18b9d18496059b5b36620e515a2d0a60fb2133023e89b85064d60c7eb=1670001892; cf_clearance=GNzGE5BUpfdl8JIyQl2ZUKlEst3nJT2.R_0ynZysf78-1669831781-0-250; _fbp=fb.2.1669835157741.1710303466; _rdt_uuid=1669835157741.e4b7d313-0fdb-4c47-83ab-4d693332e600; cfmrk_cic={"id":"tZDL9AQSa2il4ioaWODMaBpgsD5bOSnv","v1":0,"v2":0,"v3":0,"v5":0,"v7":0,"v8":0,"v6":0}; gates_cohorts=%7B%7D; CF_checkout={%227223234da8c2d1f0980f037c798387f0%22:{%22items%22:[{%22key%22:%22r2_basic%22}]}%2C%22fa8066bb9f6de3e92eaff76ec6ec9856%22:{%22items%22:[]%2C%22next%22:{%22path%22:%22/fa8066bb9f6de3e92eaff76ec6ec9856/stream%22%2C%22label%22:%22Return%20to%20Cloudflare%20Stream%22}}}; _gid=GA1.2.1733856312.1669989428; __cf_effload=1; CF_VERIFIED_DEVICE_f3efb117f44720e070094369989a5c61c3834dc123fb905940f2c92bfb692423=1670000516; vses2=b7b1ad6d2c-3kk46tqqpsqu4jldrp96ohd2bh8jk6p3; __cflb=0H28upHR6WxXGRqfrsmcyJP33mXipsFZndZRhGtCxQD; __cf_bm=WpvAExdWIFkwfo6k839GWlFori91X373iHX2OSQEuJI-1670051252-0-AR9PErqMtqub7qifUVbzGU8NvZvIwj5Qm/7WdPQvJt3xXn0lRWQOKBjDs+GIVbE8SJRO5PpcwlOv359q8SocSR8WxOKRHKfCcWCYtie5sXB6; __stripe_sid=7e9fc816-6a35-4e25-84b4-2123a4499a27840d6f",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://dash.cloudflare.com/",
    "X-Atok": "1670094193-ATOK39a339c01d919ad5df04e808263088b993de993143256e38",
    "X-Cross-Site-Security": "dash",
    "Origin": "https://dash.cloudflare.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}

# Make the DELETE request using the tag value
response = requests.delete(base_url + "/" + tag_value, headers=delete_headers)
