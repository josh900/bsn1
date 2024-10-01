# filesysteminfile

The *filesysteminfile* allows you to create and update filesystems for use as storage devices. 

**filesysteminfile IDL**

```
interface FileSystemInFile {
    constructor(String path);
    Promise<String> getFilename();
    Promise<long long> getSize();
    Promise<void> format(String fileSystem);
    Promise<void> mount();
    Promise<void> unmount();
};                                                                                                                  
```

## Object Creation

To create a *filesysteminfile* object, load the *@brightsign/filesysteminfile* module using the Node.js® require() method:

```
var FileSystemInFile = require('@brightsign/filesysteminfile');
var fsif = new FileSystemInFile("/storage/sd/usbstore.img"); // Node's native 'fs' can create an .img file                                                                                 
```

## filesysteminfile

Use this interface to configure a *filesysteminfile*.

##### getFilename()

```
Promise<String> getFilename()                                                                                                   
```

Gets the name of the file that was used to create *FileSystemInFile.*

##### getSize()

```
Promise<long long> getSize()                                                                                           
```

Retrieves the size (in bytes) of the filesystem file used to create the *FileSystemInFile* class.

##### format()

```
Promise<void> format(String fileSystem)                                                                                            
```

Creates the specified filesystem in a file that already exists. The supported filesystem types are "fat" and "exfat".

##### mount()

```
Promise<String> mount()                                                                                                 
```

Mounts the filesystem. There is no need to format the filesystem if it already exists and is formatted.

The return string is *filepath* and the return value is the path to where the filesystem has been mounted. It cannot be mounted more than once.

##### unmount()

```
Promise<void> unmount()                                                                                                 
```

Unmounts the filesystem.

## Example

The example below creates a file system, formats, mounts, and unmounts it using the npm package *fs*, 

```
const fs = require('fs');
const FileSystemInFile = require('@brightsign/filesysteminfile');

var fsif;
var fd;

open()
.then(function(fileDescriptor) {
	fd = fileDescriptor;
	return write(fd);
})
.then(function(bytes) {
	console.log(`${bytes} written to new file`);
	return close(fd);
})
.then(function() {
	// Create FileSystemInFile using the backing file
	fsif = new FileSystemInFile('/storage/sd/usbstore');

	return format();
})
.then(function() {
	return mount();
})
.then(function() {
	/* This is where you can actually do stuff with the mounted filesystem. */

	// Unmount the mounted file after 10 seconds
	setTimeout(function() {
		return unmount();
	}, 10000);
})
.catch(function(error) {
	console.log(JSON.stringify(error));
});


// Create a writable file for the file system
function open() {
	return new Promise(function(resolve, reject) {
		fs.open('/storage/sd/usbstore', 'w', function(error, fd) {
			if (error) reject(error);
			resolve(fd);
		});	
	});
};

// Write a buffer allocating 1GB of disk space for the file
function write(fd) {
	return new Promise(function(resolve, reject) {
		fs.write(fd, Buffer.alloc(1), 0, 1, (1024*1024*1024) - 1, function(error, bytesWritten) {
			if (error) reject(error);
			resolve(bytesWritten);
		});
	});
};

// Close the created file
function close(fd) {
	return new Promise(function(resolve, reject) {
		fs.close(fd, function(error) {
			if (error) reject(error);
			resolve();
		});
	});
};

// Format the file system
function format() {
	return new Promise(function(resolve, reject) {
		fsif.format("exfat")
		.then(function() {
		  console.log('Filesystem formatted');
		  resolve();
		})
		.catch(function(error) {
		  reject(error);
		});		
	});
};


// Mount the filesystem internally
function mount() {
	return new Promise(function(resolve, reject) {
		fsif.mount()
		.then(function(mount_point) {
		  console.log('Filesystem mounted' + mount_point);
		  resolve();
		})
		.catch(function(error) {
		  reject(error);
		});
	});
};

// Unmount filesystem from internal mount point. Only can unmount a mounted file
function unmount() {
	return new Promise(function(resolve, reject) {
		fsif.unmount()
		.then(function() {
		  console.log('Filesystem unmounted');
		  resolve();
		})
		.catch(function(error) {
		  reject(error);
		});
	});
};                                                                                    
```

You can also reference our public [github example](https://github.com/brightsign/usb-filesystem) which uses a BrightSign device as a filesystem over USB.