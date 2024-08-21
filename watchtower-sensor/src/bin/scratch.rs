use watchtower_sensor::message::Message;

fn main() {
    loop {
        dbg!(Message::battery().unwrap());
        dbg!(Message::cpu().unwrap());
        dbg!(Message::disk().unwrap());
        dbg!(Message::gpu().unwrap());
        dbg!(Message::net().unwrap());
        dbg!(Message::ram().unwrap());
    }
}