// config
var maxBreakpoint = 767; // maximum breakpoint
var targetID = 'navigation'; // target ID (must be present in DOM)
var triggerID = 'toggle-nav'; // trigger/button ID (will be created into targetID)

// targeting navigation
var n = document.getElementById(targetID);

// nav initially closed is JS enabled
n.classList.add('is-closed');

// global navigation function
function navi() {
    // when small screen, create a switch button, and toggle navigation class
    if (window.matchMedia("(max-width:" + maxBreakpoint +"px)").matches && document.getElementById(triggerID)==undefined) {			
        n.insertAdjacentHTML('afterBegin','<button id='+triggerID+' title="open/close navigation"></button>');
        t = document.getElementById(triggerID);  
        t.onclick=function(){ n.classList.toggle('is-closed');}
    }
    // when big screen, delete switch button, and toggle navigation class
    var minBreakpoint = maxBreakpoint + 1;
    if (window.matchMedia("(min-width: " + minBreakpoint +"px)").matches && document.getElementById(triggerID)) {
        document.getElementById(triggerID).outerHTML="";
    }
}
navi();

// when resize or orientation change, reload function
window.addEventListener('resize', navi);