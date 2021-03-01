$(window).on('load', function () {
    $('.body').css('opacity', '1');
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
            foo = $(this).html().replace(',', '.');
            total_sum += parseFloat(foo);
        });
        $('.total_sum').html(total_sum);
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
    function to_locale_string(selector) {
        $(selector).each(function () {
            let price = Number($(this).html());
            $(this).html(price.toLocaleString());
        });
    }
    // to_locale_string('.locale_string');
    // to_locale_string('.dataframe>tbody>tr>td');

    $('.winner__number').change( function () {
        let $this = $(this),
            radio = $($this).data("radio"),
            group = $($this).data("group");
        $(group).each(function () {
            $(this).attr('checked', false);
        });
        $(radio).attr('checked', true);
    });
    $('.tender__print>.col-12>.dataframe>thead').addClass('dataframe__thead');
    $('.tender__print>.col-12>.dataframe').removeClass('table').removeClass('table-striped')
    $('.tender__print>.col-12>.dataframe>tbody>tr>th').each(function () {
        $(this).css('color', '#000000');
    });
    $('#datatable').dataTable();
    $('.js-select2').select2({
        placeholder: "Введите название...",
		maximumSelectionLength: 2,
		language: "ru",
    });
});