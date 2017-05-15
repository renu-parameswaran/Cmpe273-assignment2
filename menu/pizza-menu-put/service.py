import boto3

def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("pizzashopenv")
        menu_id = {"pizzaid": event["menu_id"]}
        key = event["update"].keys()[0]
        value = event["update"][key]
        table.update_item(Key=menu_id, UpdateExpression="SET #key = :val",ExpressionAttributeNames={"#key":key}, ExpressionAttributeValues={ ":val" :value})
        return "200 OK"
    except Exception as e:
        return e.message