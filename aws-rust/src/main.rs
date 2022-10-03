use lambda_runtime::{service_fn, LambdaEvent, Error};
use serde_json::{json, Value};

// Taken From - https://github.com/awslabs/aws-lambda-rust-runtime
#[tokio::main]
async fn main() -> Result<(), Error> {
    let handler = service_fn(handler);
    lambda_runtime::run(handler).await?;
    Ok(())
}

async fn handler(event: LambdaEvent<Value>) -> Result<Value, Error> {
    let (event, _context) = event.into_parts();
    let first_name = event["firstName"].as_str().unwrap_or("world");
    println!("Respoding");
    Ok(json!({ "message": format!("Hello, {}!", first_name) }))
}