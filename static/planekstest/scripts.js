//celery progress bar
var s_frm = $('#generate-schema-form');
var s_pgrbar = $('#schema-progress-bar');

s_frm.submit(function() {
    $.ajax({
        type: s_frm.attr('method'),
        url: s_frm.attr('action'),
        data: s_frm.serialize(),
        success: function(data) {
            if (data.task_id != null) {
                get_schema_task_info(data.task_id);
            }
        },
        error: function(data) {
            console.log('Something went wrong1.')
        }
    });
    return false;
});

function get_schema_task_info(task_id) {
    $.ajax({
        type: 'get',
        url: "/schemas/get-schema-task-info/",
        data: {'task_id': task_id},
        success: function(data) {
            s_frm.html('');
            if (data.state == 'PENDING') {
                s_frm.html('Please wait...');
            } else if (data.state == 'PROGRESS' || data.state == 'SUCCESS') {
                s_pgrbar.css('display', 'inline');
                s_pgrbar.val(data.result.percent);
                s_frm.html('Rows created ' + data.result.current + ' out of ' + data.result.total);
            }
            if (data.state != 'SUCCESS') {
                setTimeout(function() {
                    get_schema_task_info(task_id)
                    }, 50)
            } else {
                s_frm.html('Done');
                $('#go-back-button').css('display', 'inline')
            }

        },
        error: function(data) {
            console.log(data)
        }
    });
}

// toggling of range integer start and end fields
$(document).ready(function () {
    toggleFields();
    $("#type").change(function () {
        toggleFields();
    });
});

function toggleFields() {
    if ($("#type").val() === "Range Integer")
        $("#range-inputs").show();
    else
        $("#range-inputs").hide();
}