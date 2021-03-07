$(document).ready(function () {
    caculateHourly();

    //$(".time-input").mask('00:00');
    $("#pnumber").mask('000000-00000');
});


$("input").click(function () {
    var value = $(this).val();
    if (value == '0') {
        $(this).val("");
    }
});

//save everything when user clicks save all data in the menu
$("#Write").click(function () {
    saveAllData();
});

//save all the data when the user updates the values
$('input').on('input', function (e) {
    //saveAllData();
});

//save all the data when the user updates the values
$('#Reload').click(function () {
    refreshNoSave();
});

function refreshNoSave() {
    location.reload();
}

$('#hourly input').keyup(function (e) {
    if (e.keyCode == 13 || e.keyCode == 9) {
        saveBlock2();
        caculateHourly();
        showMessage("Hourly information was saved");
    }
});

function saveBlock2() {
    var data = $("#hourly").serialize();
    $.ajax({
        type: "POST",
        url: "main.php",
        data: data,
        success: function (msg) {
            console.log('The hourly form was saved');
        },
        error: function (msg) {
            var message = 'Error: the data was not saved';
            console.log(message);
            alert(message);
        }
    });
}

function caculateHourly() {

    $('#hourly input[type=number]').each(function () {
        if ($(this).val().length === 0) {
            $(this).val(0);
        }

    })

    var hour1 = parseInt($('[name=hour1input]').val());
    var hour2 = parseInt($('[name=hour2input]').val());
    var hour3 = parseInt($('[name=hour3input]').val());
    var hour4 = parseInt($('[name=hour4input]').val());
    var hour5 = parseInt($('[name=hour5input]').val());
    var hour6 = parseInt($('[name=hour6input]').val());
    var hour7 = parseInt($('[name=hour7input]').val());
    var hour8 = parseInt($('[name=hour8input]').val());
    var hour9 = parseInt($('[name=hour9input]').val());
    var hour10 = parseInt($('[name=hour10input]').val());
    var hour11 = parseInt($('[name=hour11input]').val());
    var hour12 = parseInt($('[name=hour12input]').val());



    var hour1calc = hour1;
    var hour2calc = hour1 + hour2;
    var hour3calc = hour3 + hour2calc;
    var hour4calc = hour4 + hour3calc;
    var hour5calc = hour5 + hour4calc;
    var hour6calc = hour6 + hour5calc;
    var hour7calc = hour7 + hour6calc;
    var hour8calc = hour8 + hour7calc;
    var hour9calc = hour9 + hour8calc;
    var hour10calc = hour10 + hour9calc;
    var hour11calc = hour11 + hour10calc;
    var hour12calc = hour12 + hour11calc;

    // var hour2calc = hour1 + hour2;
    // var hour3calc = (hour3 != 0) ? hour3 + hour2calc : 0;
    // var hour4calc = (hour4 != 0) ? hour4 + hour3calc : 0;
    // var hour5calc = (hour5 != 0) ? hour5 + hour4calc : 0;
    // var hour6calc = (hour6 != 0) ? hour6 + hour5calc : 0;
    // var hour7calc = (hour7 != 0) ? hour7 + hour6calc : 0;
    // var hour8calc = (hour8 != 0) ? hour8 + hour7calc : 0;
    // var hour9calc = (hour9 != 0) ? hour9 + hour8calc : 0;
    // var hour10calc = (hour10 != 0) ? hour10 + hour9calc : 0;
    // var hour11calc = (hour11 != 0) ? hour11 + hour10calc : 0;
    // var hour12calc = (hour12 != 0) ? hour12 + hour11calc : 0;


    $("#calchour1").val(hour1calc);
    $("#calchour2").val(hour2calc);
    $("#calchour3").val(hour3calc);
    $("#calchour4").val(hour4calc);
    $("#calchour5").val(hour5calc);
    $("#calchour6").val(hour6calc);
    $("#calchour7").val(hour7calc);
    $("#calchour8").val(hour8calc);
    $("#calchour9").val(hour9calc);
    $("#calchour10").val(hour10calc);
    $("#calchour11").val(hour11calc);
    $("#calchour12").val(hour12calc);


}

function saveAllData() {
    saveBlock2();
    showMessage("All Data was saved");

}

function showMessage(message) {
    $(".save-message span").html(message);
    $(".save-message").fadeIn(500, function () {
        $(".save-message").delay(1000).fadeOut(500);
    });
}

function openModalWithId(modalId) {
    $("#" + modalId).fadeIn(500);
}


// get the button that backs out of modal
$('.close-modal').click(function () {
    $(".modal").fadeOut(500);
});

window.onclick = function (event) {
    if ($(event.target).hasClass("modal")) {
        $(".modal").fadeOut(500);
    }
}


$(".time-input").on('keydown', function (e) {
    if (e.keyCode == 9) {
        e.preventDefault();
        var value = $(this).val();
        if (value != null) {
            var convertedTime = convertTime(value);
            $(this).val(convertedTime);
        }
    }
});

function convertTime(time) {
    if (time.includes(":")) {
        var timeArray = time.split(":");
        hours = timeArray[0];
        if (hours > 12) {
            hours = hours - 12;
        }
        minutes = timeArray[1];

        return hours + ":" + minutes;
    }

    return "00:00";

}

