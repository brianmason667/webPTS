def application(environ,start_response):
    status = "200 OK"
    html = "<html>\n" \
           "<body>\n" \
           " horray, mod_wsgi is working\n" \
           "</body>\n" \
           "</html>\n"
    response_headder = [('Content-type','text/html')]
    start_response(status,reponse_header)
    return [html]
