client = new Paho.MQTT.Client("test.mosquitto.org",8080, "gui")

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({onSuccess:onConnect});

function onConnect(){
    console.log("onConnect");
    client.subscribe("Kaylee/#")
    message = new Paho.MQTT.Message("Face started");
    message.destinationName = "Kaylee/sys/startup";
    client.send(message);
}

function onConnectionLost(res){
    if(res.errorCode != 0) {
        console.log("onConnectionLost:"+res.errorMessage);
    }
}

function onMessageArrived(message){
    console.log("onMessageArrived:"+message.destinationName+":"+message.payloadString);
    if(message.destinationName=="Kaylee/Temp"){
        $(".temp").updateWithText(message.payloadString + '&deg; F', 1000);
    }
    else if(message.destinationName=="Kaylee/Notification"){
        if(message.payloadString.includes("remove")){
            removeNotification(message.payloadString.replace("remove", ""), 1000)
        }
        else{
            addNotification(iconTable.info, message.payloadString, 1000)
        }
        
    }
}