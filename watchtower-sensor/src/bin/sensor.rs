#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::fs::File;

use argh::FromArgs;
use serde::Deserialize;

use watchtower_sensor::message::Message;

mod http {
    use serde::Serialize;
    use watchtower_sensor::Result;

    pub fn post_json(path: &str, data: impl Serialize) -> Result<()> {
        loop {
            match ureq::post(path).send_json(&data) {
                Ok(_) => break,
                Err(_) => std::thread::sleep(std::time::Duration::from_secs(10)),
            };
        }

        Ok(())
    }
}

#[cfg(windows)]
mod tray {
    use std::process::Command;

    use tray_item::TrayItem;
    use watchtower_sensor::Result;

    pub fn add_tray_icon() -> Result<TrayItem> {
        let mut tray = TrayItem::new("Watchtower Sensor", "icon")?;

        tray.add_menu_item("Restart", || {
            Command::new(std::env::current_exe().unwrap())
                .args(std::env::args_os().skip(1))
                .spawn()
                .unwrap();

            std::process::exit(0);
        })?;

        tray.add_menu_item("Quit", || {
            std::process::exit(0);
        })?;

        Ok(tray)
    }
}

#[derive(FromArgs, Deserialize)]
#[argh(description = "watchtower sensor command-line interface")]
struct Args {
    #[argh(option)]
    #[argh(description = "backend URL")]
    hostname: String,

    #[argh(option)]
    #[argh(description = "checkin time in seconds", default = "5")]
    checkin_interval: u64,
}

fn main() -> color_eyre::Result<()> {
    color_eyre::install()?;

    let args: Args = {
        match File::open("config.json") {
            Ok(f) => serde_json::from_reader(f)?,
            Err(_) => argh::from_env(),
        }
    };

    #[cfg(windows)]
    let _tray = tray::add_tray_icon()?;


    let hostname = &args.hostname;

    let hello = Message::hello()?;
    let hello_string = format!("{hostname}/hello");

    http::post_json(&hello_string, hello)?;

    let checkin_string = format!("{hostname}/checkin");

    loop {
        http::post_json(&checkin_string, Message::battery()?)?;
        http::post_json(&checkin_string, Message::cpu()?)?;
        http::post_json(&checkin_string, Message::ram()?)?;
        http::post_json(&checkin_string, Message::net()?)?;
        http::post_json(&checkin_string, Message::gpu()?)?;
        http::post_json(&checkin_string, Message::disk()?)?;

        std::thread::sleep(std::time::Duration::from_secs(args.checkin_interval))
    }
}
