(function () {
    var formWrap = document.getElementById('fs-form-wrap');

    [].slice.call(document.querySelectorAll('select.cs-select')).forEach(function (el) {
        new SelectFx(el, {
            stickyPlaceholder: false,
            onChange: function (val) {
                document.querySelector('span.cs-placeholder').style.backgroundColor = val;
            }
        });
    });

    new FForm(formWrap, {
        onReview: function () {
            classie.add(document.body, 'overview'); // for demo purposes only
        }
    });
})();

$(window).bind("beforeunload", function () {
    console.log("length", $("#foo").val().length);
    if ($("#foo").val().length > 0)
        return "Do you really want to close?";
})

var listenerIds = new Array
    ("q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7");
var listenerString = "";
var needToConfirm = true;
function getListenerString() {
    var stringValue = "";

    for (var i = 0; i < listenerIds.length; i++) {
        if (document.getElementById(listenerIds[i])) {
            var elem = document.getElementById(listenerIds[i]);

            if (elem.type == "text" || elem.type == "number") {
                stringValue += elem.value;
            }
            else if (elem.type == "radio" || elem.type == "email") {
                if (elem.checked) {
                    stringValue += elem.value;
                }
            }
            else if (elem.type == "select-one") {
                stringValue += elem.options[elem.selectedIndex].value;
            }
            else if (elem.type == "select-multiple") {
                for (var j = 0; j < elem.options.length; j++) {
                    if (elem.options[j].selected) {
                        stringValue += elem.options[j].value;
                    }
                }
            }
        }
    }

    return stringValue;
}
function init() {
    listenerString = getListenerString();
}
function addEvent(elem, eventType, fn, useCapture) {
    if (elem.attachEvent) {
        // Internet Explorer
        var r = elem.attachEvent('on' + eventType, fn);
        return r;
    }
    else if (elem.addEventListener) {
        // Gecko
        elem.addEventListener(eventType, fn, useCapture);
        return true;
    }
    else {
        // Netscape
        elem['on' + eventType] = fn;
    }
}
function confirmExit(e) {
    if (needToConfirm && listenerString != getListenerString()) {
        var msg = "You will lose any unsaved changes.";

        if (!e) { e = window.event; }
        if (e) { e.returnValue = msg; }

        return msg;
    }
}
function setConfirmException() {
    needToConfirm = false;
}
addEvent(window, 'load', init, false);
addEvent(window, 'beforeunload', confirmExit, false);

// data de nascimento

document.getElementById("q2").addEventListener('change', function() {
  var data = new Date(this.value);
  if(isDate_(this.value) && data.getFullYear() > 1900)
      document.getElementById("q3").value = calculateAge(this.value);
});

function calculateAge(dobString) {
  var dob = new Date(dobString);
  var currentDate = new Date();
  var currentYear = currentDate.getFullYear();
  var birthdayThisYear = new Date(currentYear, dob.getMonth(), dob.getDate());
  var age = currentYear - dob.getFullYear();
  if(birthdayThisYear > currentDate) {
    age--;
  }
  return age;
}

function calcular(data) {
  var data = document.form.nascimento.value;
  alert(data);
  var partes = data.split("/");
  var junta = partes[2]+"-"+partes[1]+"-"+partes[0];
  document.form.idade.value = (calculateAge(junta));
}

var isDate_ = function(input) {
        var status = false;
        if (!input || input.length <= 0) {
          status = false;
        } else {
          var result = new Date(input);
          if (result == 'Invalid Date') {
            status = false;
          } else {
            status = true;
          }
        }
        return status;
}