#![no_std]

extern crate alloc;

use alloc::borrow::ToOwned;
use alloc::string::String;

use hex_literal::hex;

use linux_kernel_module::{cstr, println, self};

static SOMETHING: [u8; 28] = hex!("c7ebb16296e5a9a9cb202e816cd12d0ca82a5c6e54db96d6bb5e5fad");
static SPECIAL: [u8; 28] = hex!("a082d607fb9edbccaf4d4fef33b94c7ff7483d0a0bb6f3bbd42c26d0");

struct CycleFile;

impl linux_kernel_module::file_operations::FileOperations for CycleFile {
    const VTABLE: linux_kernel_module::file_operations::FileOperationsVtable =
        linux_kernel_module::file_operations::FileOperationsVtable::builder::<Self>()
            .read()
            .build();

    fn open() -> linux_kernel_module::KernelResult<Self> {
        Ok(CycleFile)
    }
}

impl linux_kernel_module::file_operations::Read for CycleFile {
    fn read(
        &self,
        _file: &linux_kernel_module::file_operations::File,
        buf: &mut linux_kernel_module::user_ptr::UserSlicePtrWriter,
        offset: u64,
    ) -> linux_kernel_module::KernelResult<()> {
        for (c, x) in SOMETHING.iter().zip(SPECIAL.iter())
            .cycle()
            .skip((offset % 9) as _)
            .take(buf.len())
        {
            buf.write(&[c ^ x])?;
        }
        Ok(())
    }
}

struct SomethingSpecialModule {
    _chrdev_registration: linux_kernel_module::chrdev::Registration,
}

impl linux_kernel_module::KernelModule for SomethingSpecialModule {
    fn init() -> linux_kernel_module::KernelResult<Self> {
        let chrdev_registration =
            linux_kernel_module::chrdev::builder(cstr!("something-special"), 0..1)?
                .register_device::<CycleFile>()
                .build()?;
        println!("Ah, now you won't forget! :)");
        Ok(SomethingSpecialModule {
            _chrdev_registration: chrdev_registration,
        })
    }
}

impl Drop for SomethingSpecialModule {
    fn drop(&mut self) {
        println!("Don't forget me!!");
    }
}

linux_kernel_module::kernel_module!(
    SomethingSpecialModule,
    author: b"Reggie Redman",
    description: b"Something special I never want to forget",
    license: b"WTFPL"
);
