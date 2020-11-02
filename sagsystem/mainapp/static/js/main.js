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
    $('.dataframe>thead>tr:first-child>th:first-child').html('Участник тендера').addClass('text-left');
    $('.dataframe>thead>tr:last-child>th:first-child').html('Товар');

    $('.dataframe>tbody>tr>td').attr('style', 'text-align: right;').each(function () {
        if ($(this).html() === 'NaN') {
            $(this).html('Нет');
        }
    });
    $('.dataframe').attr('border', '0');
    function total_sum() {
        let total_sum = 0;
        $('.price_sum').each(function () {
            total_sum += Number($(this).html());
        });
        $('.total_sum').html(String(total_sum));
    }
    total_sum();
    $('#tender_print').on('click', function (e) {
        e.preventDefault();
        e.stopImmediatePropagation;
        window.print()
    });
    $('.goods_add_optgroup').on('click', function () {
        let $this = $(this), option = $($this).data("option");
        if ($(this).hasClass('goods_opened')) {
            $(option).css('display', 'none');
            $(this).removeClass('goods_opened');
        }
        else {
            $(option).css('display', 'block');
            $(this).addClass('goods_opened');
        }
    });
});