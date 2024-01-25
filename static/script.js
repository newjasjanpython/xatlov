window.addEventListener('DOMContentLoaded', () => {
    $('input[type="text"],input[type="number"]').addClass('form-control');
    $('input[type="checkbox"]').addClass('form-check-input');
    $('textarea').addClass('form-control');
    $('textarea').attr('rows', 3);
    $('select').addClass('form-select');

    $('.form-control').each((index, elem) => {
        $(elem).on('blur', function () {
            if ($(elem).val().trim()) {
                $(elem).addClass('value');
            } else {
                $(elem).removeClass('value');
            }
        });
    });
    
    // m9GgHo
    
    let counterAm9GgHo = 2;
    $('#cloneButton-m9GgHo').on('click', function () {
        const originalCard = $('.m9GgHo-model').first();
        const newCard = originalCard.clone(true);

        newCard.find('[id]').each(function () {
            $(this).attr('id', $(this).attr('id') + '_' + counterAm9GgHo);
        });

        newCard.find('[for]').each(function () {
            $(this).attr('for', $(this).attr('for') + '_' + counterAm9GgHo);
        });

        newCard.removeData('model-id');
        newCard.find('.btn-save-m9GgHo').text("Saqlash");
        newCard.find('.form-control').val("");
        newCard.find('.form-control').removeClass('value');

        $('.m9GgHo-models').append(newCard);
        counterAm9GgHo++;
    });

    $('.m9GgHo-models').on('click', '.btn-danger', function () {
        if ($('.m9GgHo-model').length > 1) {
            $(this).closest('.m9GgHo-model').remove();
        }
    });

    $('.m9GgHo-models').on('input', 'input, textarea', function () {
        const saveButton = $(this).closest('.m9GgHo-model').find('.btn-save-m9GgHo');
        const isAnyInputEdited = $(this).closest('.m9GgHo-model').find('input, textarea').filter(function () {
            return $(this).val().trim() !== '';
        }).length > 0;

        saveButton.prop('disabled', !isAnyInputEdited);
    });

    $('.btn-save-m9GgHo').each((i, elem) => {
        $(elem).on('click', () => {
            let data = {
                "mStccp": $(elem).closest('.m9GgHo-model').find('.mStccp').val(),
                "dPmVJI": $(elem).closest('.m9GgHo-model').find('.dPmVJI').val(),
                "jZ4ndH": $(elem).closest('.m9GgHo-model').find('.jZ4ndH').val()
            }

            if ($(elem).closest('.m9GgHo-model').data('model-id') !== undefined && $(elem).closest('.m9GgHo-model').data('model-id').trim() !== '') {
                data['id'] = $(elem).closest('.m9GgHo-model').data('model-id');
                $.ajax({
                    'url': `/dev/api/problem/edit/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        $(elem).closest('.m9GgHo-model').data('model-id', String(data['id']));
                        $(elem).attr('disabled', true);
                    }
                });
            } else {
                $.ajax({
                    'url': `/dev/api/problem/create/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        if (data['status'] === 'success') {
                            $(elem).closest('.m9GgHo-model').data('model-id', String(data['id']));
                            $(elem).attr('disabled', true);
                            $(elem).text("Taxrirlash");

                            let option = document.createElement('option');
                            $(option).attr('selected', true);
                            $(option).attr('value', data['id']);

                            $('#id_m9GgHo').append(option);
                        }
                    }
                });
            }
        });
    });

    
    // L3iXGb
    let counterAL3iXGb = 2;
    
    $('#cloneButton-L3iXGb').on('click', function () {
        const originalCard = $('.L3iXGb-model').first();
        const newCard = originalCard.clone(true);

        newCard.find('[id]').each(function () {
            $(this).attr('id', $(this).attr('id') + '_' + counterAL3iXGb);
        });

        newCard.find('[for]').each(function () {
            $(this).attr('for', $(this).attr('for') + '_' + counterAL3iXGb);
        });

        newCard.removeData('model-id');
        newCard.find('.btn-save-L3iXGb').text("Saqlash");
        newCard.find('.form-control').val("");
        newCard.find('.form-control').removeClass('value');

        $('.L3iXGb-models').append(newCard);
        counterAL3iXGb++;
    });

    $('.L3iXGb-models').on('click', '.btn-danger', function () {
        if ($('.L3iXGb-model').length > 1) {
            $(this).closest('.L3iXGb-model').remove();
        }
    });

    $('.L3iXGb-models').on('input', 'input, textarea', function () {
        const saveButton = $(this).closest('.L3iXGb-model').find('.btn-save-L3iXGb');
        const isAnyInputEdited = $(this).closest('.L3iXGb-model').find('input, textarea').filter(function () {
            return $(this).val().trim() !== '';
        }).length > 0;

        saveButton.prop('disabled', !isAnyInputEdited);
    });

    $('.btn-save-L3iXGb').each((i, elem) => {
        $(elem).on('click', () => {
            let data = {
                "jqfJ4u": $(elem).closest('.L3iXGb-model').find('.jqfJ4u').val(),
                "GWUmHY": $(elem).closest('.L3iXGb-model').find('.GWUmHY').val(),
                "KzVEbd": $(elem).closest('.L3iXGb-model').find('.KzVEbd').val(),
            }

            console.log(data);

            if ($(elem).closest('.L3iXGb-model').data('model-id') !== undefined && $(elem).closest('.L3iXGb-model').data('model-id').trim() !== '') {
                data['id'] = $(elem).closest('.L3iXGb-model').data('model-id');
                $.ajax({
                    'url': `/dev/api/member_inf/edit/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        $(elem).closest('.L3iXGb-model').data('model-id', String(data['id']));
                        $(elem).attr('disabled', true);
                    },
                    error: (err) => { console.error(err); }
                });
            } else {
                $.ajax({
                    'url': `/dev/api/member_inf/create/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        if (data['status'] === 'success') {
                            $(elem).closest('.L3iXGb-model').data('model-id', String(data['id']));
                            $(elem).attr('disabled', true);
                            $(elem).text("Taxrirlash");

                            let option = document.createElement('option');
                            $(option).attr('selected', true);
                            $(option).attr('value', data['id']);

                            $('#id_L3iXGb').append(option);
                        }
                    },
                    error: (err) => { console.error(err); }
                });
            }
        });
    });

    
    // d0Gawy
    let counterAd0Gawy = 2;
    
    $('#cloneButton-d0Gawy').on('click', function () {
        const originalCard = $('.d0Gawy-model').first();
        const newCard = originalCard.clone(true);

        newCard.find('[id]').each(function () {
            $(this).attr('id', $(this).attr('id') + '_' + counterAd0Gawy);
        });

        newCard.find('[for]').each(function () {
            $(this).attr('for', $(this).attr('for') + '_' + counterAd0Gawy);
        });

        newCard.removeData('model-id');
        newCard.find('.btn-save-d0Gawy').text("Saqlash");
        newCard.find('.form-control').val("");
        newCard.find('.form-control').removeClass('value');

        $('.d0Gawy-models').append(newCard);
        counterAd0Gawy++;
    });

    $('.d0Gawy-models').on('click', '.btn-danger', function () {
        if ($('.d0Gawy-model').length > 1) {
            $(this).closest('.d0Gawy-model').remove();
        }
    });

    $('.d0Gawy-models').on('input', 'input, textarea', function () {
        const saveButton = $(this).closest('.d0Gawy-model').find('.btn-save-d0Gawy');
        const isAnyInputEdited = $(this).closest('.d0Gawy-model').find('input, textarea').filter(function () {
            return $(this).val().trim() !== '';
        }).length > 0;

        saveButton.prop('disabled', !isAnyInputEdited);
    });

    $('.btn-save-d0Gawy').each((i, elem) => {
        $(elem).on('click', () => {
            let data = {
                "A3TP8D": $(elem).closest('.d0Gawy-model').find('.A3TP8D').val(),
                "aiJCTv": $(elem).closest('.d0Gawy-model').find('.aiJCTv').val()
            }

            if ($(elem).closest('.d0Gawy-model').data('model-id') !== undefined && $(elem).closest('.d0Gawy-model').data('model-id').trim() !== '') {
                data['id'] = $(elem).closest('.d0Gawy-model').data('model-id');
                $.ajax({
                    'url': `/dev/api/member_in_note/edit/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        $(elem).closest('.d0Gawy-model').data('model-id', String(data['id']));
                        $(elem).attr('disabled', true);
                    },
                    error: (err) => { console.error(err); }
                });
            } else {
                $.ajax({
                    'url': `/dev/api/member_in_note/create/`,
                    'method': 'POST',
                    'data': data,
                    'dataType': 'json',
                    success: (data) => {
                        if (data['status'] === 'success') {
                            $(elem).closest('.d0Gawy-model').data('model-id', String(data['id']));
                            $(elem).attr('disabled', true);
                            $(elem).text("Taxrirlash");

                            let option = document.createElement('option');
                            $(option).attr('selected', true);
                            $(option).attr('value', data['id']);

                            $('#id_d0Gawy').append(option);
                        }
                    },
                    error: (err) => { console.error(err); }
                });
            }
        });
    });
});