use std::process::Command;

fn main() {
    #[cfg(windows)]
    windres::Build::new().compile("sensor.rc").unwrap();


    #[cfg(windows)]
    windres::Build::new().compile("sensor.rc").unwrap();

    // macOS installer creation
    #[cfg(target_os = "macos")]
    {
        // Run your shell commands to create the installer
        let status = Command::new("sh")
            .arg("-c")
            .arg("
                mkdir -p distribution/Applications
                cp target/release/sensor distribution/Applications/
                cp config.json distribution/Applications/
                pkgbuild --root distribution --identifier com.your_company.watchtower_sensor --version 0.1 watchtower_sensor.pkg
                productbuild --synthesize --package watchtower_sensor.pkg distribution.xml
                productbuild --distribution distribution.xml --package-path . final_installer.pkg
            ")
            .status()
            .unwrap();

        assert!(status.success());
    }
}