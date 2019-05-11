from mitmproxy import flow
from mitmproxy import http
import cgi
import re
from gzip import GzipFile
from io import StringIO
import time

XML_OK_RESPONSE = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>iPhone 1,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone1,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone2,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone3,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone3,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 3,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone4,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone5,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone5,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone5,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone5,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 6,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 6,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 7,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 7,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 8,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 8,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 8,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 9,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 9,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 9,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 9,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 10,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 11,8</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 11,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 11,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPhone 11,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad1,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad3,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad5,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad5,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,7</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,8</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,11</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad6,12</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad7,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,7</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad8,8</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad11,3</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad11,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad2,7</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,4</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,5</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,6</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,7</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,8</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad4,9</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad5,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad5,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad11,1</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
        <key>iPad11,2</key>
        <array>
            <string>powerDiagnostics</string>
        </array>
    </dict>
    </plist>
'''

def request(context, flow):
    path = flow.request.path  
    print('Path is %s' % path)
    if path == '/ios/TestConfiguration/1.2':
        respond(flow, XML_OK_RESPONSE)  
    elif path == '/MR3Server/ValidateTicket?ticket_number=123456':    
        respond(flow, XML_OK_RESPONSE)
    elif path == '/MR3Server/MR3Post':
        saveContent(flow, 'general')
        respond(flow, XML_OK_RESPONSE)
    elif path == '/ios/log/extendedUpload':
        saveContent(flow, 'power')
        respond(flow, XML_OK_RESPONSE)


def saveContent(flow, prefix):
    decodedData = StringIO.StringIO()
    decodedData.write(flow.request.get_decoded_content())

    mimeType = flow.request.headers.get('Content-Type', '')
    multipart_boundary_re = re.compile('^multipart/form-data; boundary=(.*)$')
    matches = multipart_boundary_re.match(mimeType) 

    decodedData.seek(0)

    query = cgi.parse_multipart( decodedData, {"boundary" : matches.group(1)})

    with open("%s-%s.tar.gz" % (prefix, time.strftime("%Y%m%d-%H%M%S")), "w") as logs:
        logs.write(query['log_archive'][0])

def respond(flow, content):
    resp = HTTPResponse("HTTP/1.1", 200, "OK",
                        Headers(Content_Type="text/xml"),
                        content)
    flow.reply(resp)

