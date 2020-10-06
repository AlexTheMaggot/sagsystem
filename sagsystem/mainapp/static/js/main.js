$(window).on('load', function () {
    $(".modal_modal").each(function () {
        $(this).wrap('<div class="overlay"></div>')
    });

    $(".open-modal_modal").on('click', function (e) {
        e.preventDefault();
        e.stopImmediatePropagation;

        let $this = $(this),
            modal_modal = $($this).data("modal_modal");

        $(modal_modal).parents(".overlay").addClass("open");
        setTimeout(function () {
            $(modal_modal).addClass("open");
        }, 350);

        $(document).on('click', function (e) {
            let target = $(e.target);

            if ($(target).hasClass("overlay")) {
                $(target).find(".modal_modal").each(function () {
                    $(this).removeClass("open");
                });
                setTimeout(function () {
                    $(target).removeClass("open");
                }, 350);
            }

        });

    });
    $(".close-modal_modal").on('click', function (e) {
        e.preventDefault();
        e.stopImmediatePropagation;

        let $this = $(this),
            modal_modal = $($this).data("modal_modal");

        $(modal_modal).removeClass("open");
        setTimeout(function () {
            $(modal_modal).parents(".overlay").removeClass("open");
        }, 350);
    });
    $('#add_product').on('click', function (e) {
        if ($('.tenders-new__input').val() === '') {
            e.preventDefault();
        }
    });
});