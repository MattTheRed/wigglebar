
function addClick (element, func) {
    if (element.addEventListener) {
        element.addEventListener('click', func);
    }
    else if (element.attachEvent) {
        element.attachEvent('onclick', func);
    }
}


var nb = new Object;

nb.init = function (barId) {
    console.log("running");
    barId = barId || 0;
    if (barId == 0) {
        nb.setColorsAndContent(demo=true);
    } else {
        var head = document.getElementsByTagName("HEAD")[0];
        nb.initialize = document.createElement("SCRIPT");
        nb.initialize.type="text/javascript";
        nb.initialize.src = "//www.wigglebar.com/view/"+ barId + "/initialize.js";
        head.appendChild(nb.initialize);
    }

};
//
//
nb.setColorsAndContent = function (demo, colors, content) {
    demo = demo || false;
    colors = colors || {};
    content = content || {};
    console.log(demo);
    if (demo) {
        console.log("in here");
        nb.messageText = "[[content.messageText]]";
        nb.buttonText = "[[content.buttonText]]";
        nb.buttonLink = "[[content.buttonLink]]";
        nb.iconUrl = "[[content.iconUrl]]";

        nb.backgroundColor = "[[colors.background]]";
        nb.textColor = "[[colors.text]]";
        nb.buttonBackgroundColor = "[[colors.buttonBackground]]";
        nb.buttonTextColor = "[[colors.buttonText]]";
        //nb.iconBackgroundColor = "[[colors.iconBackground]]";

    }

    else {
        console.log(content.messageText);
        nb.messageText = content.messageText;
        nb.buttonText = content.buttonText;
        nb.buttonLink = content.buttonLink;
        nb.iconUrl = content.iconUrl;

        nb.backgroundColor = colors.background;
        nb.textColor = colors.text;
        nb.buttonBackgroundColor = colors.buttonBackground;
        nb.buttonTextColor = colors.buttonText;

    }
    nb.addBar();


}
nb.addBar  = function (){
    var head = document.getElementsByTagName("HEAD")[0];
    nb.logoFont = document.createElement("LINK");
    nb.logoFont.href = "//fonts.googleapis.com/css?family=Great+Vibes";
    nb.logoFont.rel="stylesheet";
    nb.logoFont.type="text/css";
    head.appendChild(nb.logoFont);

    nb.barStyles = document.createElement("LINK");
    nb.barStyles.href = "//pindar.s3.amazonaws.com/css/notifybar/viewer/bar.css";
    nb.barStyles.rel="stylesheet";
    nb.barStyles.type="text/css";
    head.appendChild(nb.barStyles);

    nb.offsetBar = document.createElement("DIV");
    nb.offsetBar.id = "nb-offset-bar";
    document.body.insertBefore(nb.offsetBar, document.body.firstChild);
    nb.offsetBar.className = "nb-offset-bar nb-hide-offset";


    // var styleSheet=document.createElement("STYLE");
    // styleSheet.type = "text/css";
    // styleSheet.appendChild(document.createTextNode(styles));

    // head.appendChild(styleSheet);

    // var body = document.getElementsByTagName("BODY")[0];
    // console.log(body.style.marginTop);
    // body.style.marginTop = "60px"; // This should be fixed
    // marginTop = window.getComputedStyle(body).getPropertyValue("margin-top");
    // console.log(marginTop);
    // var newMargin;
    // if (!marginTop) {
    //     console.log("not set");
    //     body.style.marginTop = "60px";
    // } else {
    //     marginTopNumber = parseInt(marginTop) + 60;
    //     marginTopUnits = marginTop.split(marginTopNumber)[1];
    //     body.style.marginTop = String(marginTopNumber + marginTopUnits);
    // }

    nb.bar=document.createElement("DIV");
    document.body.insertBefore(nb.bar, document.body.firstChild);
    nb.bar.className = "nb-notification-bar nb-hide";
    nb.bar.id ="nb-notification-bar";
    nb.bar.setAttribute("style", "background-color:" + nb.backgroundColor + ";");

    nb.closeLink = document.createElement("A");
    nb.closeLink.innerHTML = "x";
    nb.closeLink.href = "#";
    nb.closeLink.className = "nb-x";
    nb.closeLink.onclick = function () {
        this.parentNode.parentNode.removeChild(this.parentNode);
        document.getElementById('nb-offset-bar').parentNode.removeChild(document.getElementById('nb-offset-bar'));
    };
    nb.closeLink.setAttribute("style", "color:" + nb.textColor + ";");
    nb.bar.appendChild(nb.closeLink);

    nb.logo = document.createElement("DIV");
    nb.logo.className="nb-logo";
    nb.logo.innerHTML = '<a href="http://www.wigglebar.com" target="_blank">WiggleBar</a>';
    nb.bar.appendChild(nb.logo);

    nb.barContent=document.createElement("DIV");
    nb.barContent.className = "nb-notification-bar-content";
    nb.bar.appendChild(nb.barContent);

    nb.barMessage=document.createElement("DIV");
    nb.barMessage.className = "nb-bar-message";
    nb.barContent.appendChild(nb.barMessage);

    nb.imgLink = document.createElement("A");
    nb.imgLink.href = nb.buttonLink;
    nb.imgLink.className = "nb-bar-img-link wiggle-link";
    //nb.imgLink.setAttribute("style", "background-color:" + nb.iconBackgroundColor + ";");
    nb.barMessage.appendChild(nb.imgLink);


    nb.img = document.createElement("IMG");
    nb.img.src = nb.iconUrl;
    nb.img.className = "nb-bar-img";
    nb.imgLink.appendChild(nb.img);

    nb.barMessageText=document.createElement("SPAN");
    nb.barMessageText.className = "nb-bar-message-text";
    nb.barMessageText.innerHTML =  nb.messageText;
    nb.barMessageText.setAttribute("style", "color:" + nb.textColor + ";");
    nb.barMessage.appendChild(nb.barMessageText);

    nb.barButtonContainer = document.createElement("DIV");
    nb.barButtonContainer.className = "nb-bar-button-container";
    nb.bar.appendChild(nb.barButtonContainer);

    nb.barButton = document.createElement("A");
    nb.barButton.href = nb.buttonLink;
    nb.barButton.setAttribute("style", "background-color:" + nb.buttonBackgroundColor +
        "; color:" + nb.buttonTextColor + ";");
    nb.barButton.className = "nb-button wiggle-link";
    nb.barButton.innerHTML = nb.buttonText;
    nb.barButtonContainer.appendChild(nb.barButton);

    setTimeout(nb.slideDown,900);
    setTimeout(function () {
        nb.wiggleElement(nb.img, "long-wiggle")
    }, 1600);

    setTimeout(function () {
        nb.wiggleElement(nb.barButtonContainer, "long-wiggle")
    }, 35000);

    setTimeout(function () {
        nb.wiggleElement(nb.barButtonContainer, "long-wiggle")
    }, 70000);
};

nb.slideDown = function () {
    nb.offsetBar.className = "nb-offset-bar";
    nb.bar.className = "nb-notification-bar";
};

nb.wiggleElement = function (element, wiggleType) {
    wiggleType = wiggleType || " wiggle ";

    if (element.className.indexOf(wiggleType) != -1) {
        element.className = element.className.replace(wiggleType, "");
    }

    setTimeout(function (){
        element.className += " " + wiggleType;
    }, 10)
}


nb.changeColors = function (background, text, buttonBackground, buttonText, icon) {
    icon = icon || "#ffffff";
    console.log(icon);
    nb.bar.setAttribute("style", "background-color:" + background + ";");
    nb.barMessage.setAttribute("style", "color:" + text + ";");
    nb.barButton.setAttribute("style", "background-color:" + buttonBackground + "; color:" + buttonText + ";");
};

nb.changeMessage = function (message) {
    console.log("changing");
    nb.barMessageText.innerHTML = message;
};

