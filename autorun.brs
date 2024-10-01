Sub Main()
    print "Unpacking autorun.zip..."
    
    za = CreateObject("roZipArchive")
    if za.Install("autorun.zip") then
        print "Successfully unpacked autorun.zip"
    else
        print "Failed to unpack autorun.zip"
    endif
    
    RebootSystem()
End Sub