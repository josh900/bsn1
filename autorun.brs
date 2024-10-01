Sub Main()
    print "Starting web app..."
    
    ' Create and configure the HTML widget
    r = CreateObject("roRectangle", 0, 0, 1920, 1080)
    config = {
        nodejs_enabled: true,
        inspector_server: { port: 3000 },
        brightsign_js_objects_enabled: true,
        url: "file:///sd:/index.html"
    }
    
    h = CreateObject("roHtmlWidget", r, config)
    h.Show()
    
    ' Event loop
    port = CreateObject("roMessagePort")
    h.SetPort(port)
    
    while true
        msg = wait(0, port)
        if type(msg) = "roHtmlWidgetEvent" then
            print "HTML widget event: "; msg.GetData()
        endif
    end while
End Sub