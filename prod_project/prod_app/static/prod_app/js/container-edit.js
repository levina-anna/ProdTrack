// Отправляем id на сервер и получаем данные для модульного окна
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.container-row').forEach(row => {
        row.addEventListener('click', function() {
            // Получаем ID контейнера
            const containerId = this.dataset.containerId;
            // console.log("Container for editing: ", containerId)

            if (containerId) {
                fetch(`/get_container_data/${containerId}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Container not found');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log("Data from the server: ", data)
                        setData(data);
                        const modalBody = document.querySelector('#editContainerModal .modal-body');
                        var modal = new bootstrap.Modal(document.getElementById('editContainerModal'));
                        modal.show();
                    })
                    .catch(error => {
                    console.error('Error:', error);
                    });
            } else {
                    console.error('Container ID not defined.');
                    }
        });
    });
});


// Функция для заполнения формы полученными  данными от сервера
function setData(data) {
    console.log("Данные для заполнения формы:", data);

    // Заполняем статичные текстовые поля
    document.getElementById('containerIdModal').textContent = data.id;
    document.getElementById('containerNumberModal').textContent = data.container_number;
    document.getElementById('productionDateModal').textContent = data.batch__date_produced;

    // Устанавливаем значение для поля "Volume"
    document.getElementById('containerWeightModal').value = parseFloat(data.volume);

    // Устанавливаем выбранное значение в выпадающем списке "Product type"
    const productTypeSelect = document.getElementById('productTypeModal');
    Array.from(productTypeSelect.options).forEach(option => {
        option.selected = (option.textContent === data.chemical__name);
    });

    // Устанавливаем чекбокс "Recyclable"
    document.getElementById('isRecyclableModal').checked = data.is_recyclable;

    // Устанавливаем значение ползунка "Purity level"
    document.getElementById('purityLevelModal').value = data.purity_level;

    // Устанавливаем радиокнопки "Storage condition"
    const storageConditionRadios = document.getElementsByName('storageCondition');
    storageConditionRadios.forEach(radio => {
        if (radio.value === data.storage_condition) {
            radio.checked = true;
        }
    });

    // Заполняем текстовое поле "Notes"
    document.getElementById('notesModal').value = data.notes;
}


// Отправка обновленных данных на сервер
document.getElementById('editContainerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Собираем данные
    const formData = {
        id: document.getElementById('containerIdModal').textContent,
        container_number: document.getElementById('containerNumberModal').textContent,
        date_produced: document.getElementById('productionDateModal').textContent,
        chemical_name: document.getElementById('productTypeModal').value,
        volume: parseFloat(document.getElementById('containerWeightModal').value),
        is_recyclable: document.getElementById('isRecyclableModal').checked,
        purity_level: parseInt(document.getElementById('purityLevelModal').value),
        storage_condition: document.querySelector('input[name="storageCondition"]:checked').value,
        notes: document.getElementById('notesModal').value
    };

    console.log("Data for sending (for updating):", formData)

    // Отправляем данные на сервер
    fetch(`/update_container_data/${formData.id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // alert('Data updated successfully');
        console.log('Data updated successfully');
        // Закрываем модальное окно
        var modal = bootstrap.Modal.getInstance(document.getElementById('editContainerModal'));
        modal.hide();

        // Обновляем страницу
        window.location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred while updating data');
    });
});