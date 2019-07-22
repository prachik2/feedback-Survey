$(document).ready(function () {

    var navListItems = $('div.setup-panel div a'),
        allWells = $('.setup-content'),
        allNextBtn1 = $('.nextBtn1');
        allNextBtn2 = $('.nextBtn2');
        allNextEditBtn = $('.nexteditBtn');
        createBtn = $('.createBtn');
        backBtn1 = $('.back1');
        backBtn2 = $('.back2');
        // error = "{{error}}"
        // console.log("error",error)

    allWells.hide();

    navListItems.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr('href')),
        
            $item = $(this);
        if (!$item.hasClass('disabled')) {
            navListItems.removeClass('btn-success').addClass('btn-default');
            $item.addClass('btn-success');
            allWells.hide();
            $target.show();
            $target.find('input:eq(0)').focus();
        }
    });

    backBtn1.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr('href')),
        
        $item = $(".step-1");
        $item1 = $(".step-2");

        $item1.removeClass('btn-success').addClass('btn-default');
        $item.addClass('btn-success');
        allWells.hide();
        $target.show();
        $target.find('input:eq(0)').focus();
        
    });

    backBtn2.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr('href')),
        
        $item = $(".step-2");
        $item1 = $(".step-3");

        $item1.removeClass('btn-success').addClass('btn-default');
        $item.addClass('btn-success');
        allWells.hide();
        $target.show();
        $target.find('input:eq(0)').focus();
        
    });

    // if(error)
    // {
    //     e.preventDefault();
    //     var $target = $($(this).attr('href')),
        
    //     // $item = $(".step-2");
    //     $item1 = $(".step-3");

    //     // $item1.removeClass('btn-success').addClass('btn-default');
    //     $item1.addClass('btn-success');
    //     allWells.hide();
    //     $item1.show();
    //     // $target.find('input:eq(0)').focus();

    // }

    allNextBtn1.click(function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
            curInputs = curStep.find("input[type='text'],input[type='url'],select,input[type='email']")
            isValid = true;

        $(".form-group").removeClass("has-error");
        for (var i = 0; i < curInputs.length; i++) {
            if (!curInputs[i].validity.valid) {
                isValid = false;
                $(curInputs[i]).closest(".form-group").addClass("has-error");
            }
        }

        if (isValid) nextStepWizard.removeAttr('disabled').trigger('click');
    });

    allNextBtn2.on('click',function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
            curInputs = curStep.find("input[type='text'],input[type='url'],select")
            isValid = true;

        $(".form-group").removeClass("has-error");
        var z = $('#addressTable').DataTable();
        if(z.data().count() < 1)
        {
            for (var i = 0; i < curInputs.length; i++) {
                if (!curInputs[i].validity.valid) {
                    isValid = false;
                    $(curInputs[i]).closest(".form-group").addClass("has-error");
                }
            }
        }

        else
        {
           if (isValid) nextStepWizard.removeAttr('disabled').trigger('click'); 
        }

        
    });
    allNextEditBtn.on('click',function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
            curInputs = curStep.find("input[type='text'],input[type='url'],select")
            isValid = true;

        $(".form-group").removeClass("has-error");
        var e = $('#editaddressTable').DataTable();
        if(e.data().count() < 1)
        {
            for (var i = 0; i < curInputs.length; i++) {
                if (!curInputs[i].validity.valid) {
                    isValid = false;
                    $(curInputs[i]).closest(".form-group").addClass("has-error");
                }
            }
        }

        else
        {
           if (isValid) nextStepWizard.removeAttr('disabled').trigger('click'); 
        }

        
    });
    createBtn.on('click',function () {
        console.log("Clicked Create Button Class")
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),           
            curInputs = curStep.find("input[type='text'],input[type='url'],select")
            isValid = true;

        $(".form-group").removeClass("has-error");
        var e = $('#bankTable').DataTable();
        if(e.data().count() < 1)
        {
            for (var i = 0; i < curInputs.length; i++) {
                if (!curInputs[i].validity.valid) {
                    isValid = false;
                    $(curInputs[i]).closest(".form-group").addClass("has-error");
                }
            }
        }

        else
        {
           if (isValid) nextStepWizard.removeAttr('disabled').trigger('click'); 
        }
        
    });

    $('div.setup-panel div a.btn-success').trigger('click');
});