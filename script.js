document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.querySelector('table.table-bordered tbody');
    const clearTableBtn = document.querySelector('.btn-danger.mx-2'); // Clear Table button
    const addPersonBtn = document.querySelector('.btn-primary.mx-2'); // Add Person button
    const distributeTipsBtn = document.querySelector('.btn-success.mx-2'); // Distribute Tips button
    const generateReportBtn = document.querySelector('.btn-info.mx-2'); // Generate Report button
    const cashInput = document.getElementById('cash');
    const cardInput = document.getElementById('card');
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const toggleSwitch = document.getElementById('threePercentToggle');
    const toggleStatus = document.getElementById('toggleStatus');
    const datePicker = document.getElementById('date-picker');

    const cashComparison = document.getElementById('cashComparison');
    const cardComparison = document.getElementById('cardComparison');
    const cashOriginal = document.getElementById('cashOriginal');
    const cardOriginal = document.getElementById('cardOriginal');
    const cashReduced = document.getElementById('cashReduced');
    const cardReduced = document.getElementById('cardReduced');
    const cashDifference = document.getElementById('cashDifference');
    const cardDifference = document.getElementById('cardDifference');

    // Set the date picker to today's date by default
    const today = new Date().toISOString().split('T')[0]; 
    datePicker.value = today; 

    // Column names in the table
    const headers = [
        'Employee',
        'Job Title',
        'Payable Hours',
        'Cash Tips',
        'Credit Card Tips',
        'Total Tips',
        'Initial Hourly Wage',
        'Wage Adjustment',
        'Adjusted Hourly Wage'
    ];

    // Columns that should have input fields
    const inputFields = ['Employee', 'Job Title', 'Payable Hours'];

    // Required columns from the file
    const REQUIRED_COLUMNS = ['Employee', 'Job Title', 'Payable Hours'];

    // Function to create a new empty row
    function createEmptyRow() {
        const row = document.createElement('tr');
        headers.forEach(header => {
            const td = document.createElement('td');
            if (inputFields.includes(header)) {
                const input = document.createElement('input');
                input.placeholder = header;
                if (header === 'Payable Hours') {
                    input.type = 'number';
                    input.step = '0.01';
                } else {
                    input.type = 'text';
                }
                td.appendChild(input);
            } else {
                td.textContent = '-';
            }
            row.appendChild(td);
        });
        return row;
    }

    // On page load, start with one empty row if none present
    if (tableBody.querySelectorAll('tr').length === 0) {
        tableBody.appendChild(createEmptyRow());
    }

    // Function to perform distribution
    function performDistribution() {
        let cashValue = parseFloat(cashInput.value) || 0;
        let cardValue = parseFloat(cardInput.value) || 0;

        // If 3% deduction is applied
        if (toggleSwitch.checked) {
            cashValue = cashValue * 0.97;
            cardValue = cardValue * 0.97;
        }

        // Calculate total hours
        let totalHours = 0;
        const rows = tableBody.querySelectorAll('tr');
        rows.forEach(row => {
            const hoursInput = row.cells[2].querySelector('input');
            const hours = parseFloat(hoursInput ? hoursInput.value : 0) || 0;
            totalHours += hours;
        });

        if (totalHours === 0) {
            // If there are no hours, we can't distribute, just return
            return;
        }

        // Distribute tips to each person
        rows.forEach(row => {
            const hoursInput = row.cells[2].querySelector('input');
            const hours = parseFloat(hoursInput ? hoursInput.value : 0) || 0;
            const ratio = (hours / totalHours) || 0;

            // Calculate individual's share of tips
            const personCashTips = cashValue * ratio;
            const personCardTips = cardValue * ratio;
            const totalTips = personCashTips + personCardTips;

            // Calculate total earned and initial hourly wage
            const basePay = hours * 10; // $10/hour base
            const totalEarned = basePay + totalTips;
            const initialHourlyWage = hours > 0 ? (totalEarned / hours) : 0;

            // Determine wage adjustment if needed
            let wageAdjustment = '-';
            let adjustedHourlyWage = '-';
            if (initialHourlyWage < 15 && hours > 0) {
                const x = (15 * hours) - totalEarned;
                wageAdjustment = x.toFixed(2);
                adjustedHourlyWage = '15.00';
            }

            // Populate the row
            row.cells[3].textContent = personCashTips.toFixed(2);     // Cash Tips
            row.cells[4].textContent = personCardTips.toFixed(2);     // Credit Card Tips
            row.cells[5].textContent = totalTips.toFixed(2);          // Total Tips
            row.cells[6].textContent = initialHourlyWage.toFixed(2);  // Initial Hourly Wage
            row.cells[7].textContent = wageAdjustment;                // Wage Adjustment
            row.cells[8].textContent = adjustedHourlyWage;            // Adjusted Hourly Wage
        });
    }

    // Clear Table button functionality
    clearTableBtn.addEventListener('click', function () {
        // Remove all rows
        tableBody.innerHTML = '';
        // Add one empty row again
        tableBody.appendChild(createEmptyRow());
        // Clear the cash and card inputs
        cashInput.value = '';
        cardInput.value = '';

        // Turn off the 3% toggle
        toggleSwitch.checked = false;
        toggleStatus.innerHTML = '3% deduction is <strong>NOT</strong> applied.';
        cashComparison.classList.add('d-none');
        cardComparison.classList.add('d-none');
    });

    // Add Person button functionality
    addPersonBtn.addEventListener('click', function () {
        // Add a new empty row
        tableBody.appendChild(createEmptyRow());
    });

    // Distribute Tips button functionality
    distributeTipsBtn.addEventListener('click', function () {
        performDistribution();
    });

    // Generate Report button functionality
    generateReportBtn.addEventListener('click', function () {
        const table = document.querySelector('table.table-bordered');
        let tableHTML = table.outerHTML.replace(/ /g, '%20');
        let dataType = 'application/vnd.ms-excel';

        // Get the date from the date picker for the filename
        let selectedDate = datePicker.value || today;
        let filename = 'Tip Allocation ' + selectedDate + '.xls';

        let downloadLink = document.createElement('a');
        document.body.appendChild(downloadLink);

        downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
        downloadLink.download = filename;
        downloadLink.click();
        document.body.removeChild(downloadLink);
    });

    // Drag and Drop / File Upload Functionality
    dropArea.addEventListener('click', () => fileInput.click());
    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.classList.add('bg-light');
    });
    dropArea.addEventListener('dragleave', () => dropArea.classList.remove('bg-light'));
    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.classList.remove('bg-light');
        const file = e.dataTransfer.files[0];
        processFile(file);
    });
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        processFile(file);
    });

    function processFile(file) {
        const fileExtension = file.name.split('.').pop().toLowerCase();

        if (fileExtension === 'xlsx' || fileExtension === 'xls') {
            processExcelFile(file);
        } else if (fileExtension === 'csv') {
            processCSVFile(file);
        } else {
            alert('Unsupported file format. Please upload an Excel or CSV file.');
        }
    }

    function processExcelFile(file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const data = new Uint8Array(event.target.result);
            const workbook = XLSX.read(data, { type: 'array' });
            const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
            const jsonData = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });
            populateTable(jsonData);
        };
        reader.readAsArrayBuffer(file);
    }

    function processCSVFile(file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const csvData = event.target.result;
            Papa.parse(csvData, {
                complete: function (results) {
                    // results.data is an array of arrays
                    populateTable(results.data);
                },
                header: false,
                skipEmptyLines: true
            });
        };
        reader.readAsText(file);
    }

    function populateTable(data) {
        // data is an array of arrays representing rows
        // First row should be header row
        if (data.length === 0) {
            alert("The file is empty or not formatted correctly.");
            return;
        }

        // Extract headers from first row
        const fileHeaders = data[0].map(h => (h ? h.toString().trim() : ''));
        
        // Find the indexes of required columns
        const employeeIndex = fileHeaders.indexOf('Employee');
        const jobIndex = fileHeaders.indexOf('Job Title');
        const hoursIndex = fileHeaders.indexOf('Payable Hours');

        // Check if all required columns exist
        if (employeeIndex === -1 || jobIndex === -1 || hoursIndex === -1) {
            alert("The uploaded file must have 'Employee', 'Job Title', and 'Payable Hours' columns in the header.");
            return;
        }

        // Clear existing rows
        tableBody.innerHTML = '';

        // Process data rows (skip the header row)
        for (let i = 1; i < data.length; i++) {
            const rowData = data[i];
            if (!rowData || rowData.length === 0) continue;

            // Extract values from the identified columns, default to empty string if undefined
            const employeeValue = rowData[employeeIndex] || '';
            const jobValue = rowData[jobIndex] || '';
            const hoursValue = rowData[hoursIndex] || '';

            // Create a new row
            const tr = document.createElement('tr');

            // employee column
            let td = document.createElement('td');
            let input = document.createElement('input');
            input.type = 'text';
            input.value = employeeValue;
            td.appendChild(input);
            tr.appendChild(td);

            // Job Title column
            td = document.createElement('td');
            input = document.createElement('input');
            input.type = 'text';
            input.value = jobValue;
            td.appendChild(input);
            tr.appendChild(td);

            // Payable Hours column
            td = document.createElement('td');
            input = document.createElement('input');
            input.type = 'number';
            input.step = '0.01';
            input.value = hoursValue;
            td.appendChild(input);
            tr.appendChild(td);

            // Remaining columns as dashes
            for (let j = 3; j < 9; j++) {
                const dashTd = document.createElement('td');
                dashTd.textContent = '-';
                tr.appendChild(dashTd);
            }

            tableBody.appendChild(tr);
        }

        // If table is empty after upload (no data rows), add one empty row
        if (tableBody.querySelectorAll('tr').length === 0) {
            tableBody.appendChild(createEmptyRow());
        }
    }

    // 3% Toggle Switch
    toggleSwitch.addEventListener('change', () => {
        const cashValue = parseFloat(cashInput.value) || 0;
        const cardValue = parseFloat(cardInput.value) || 0;

        if (toggleSwitch.checked) {
            toggleStatus.innerHTML = '3% deduction is <strong>APPLIED</strong>.';

            // Calculate reduced values
            const cashReducedVal = (cashValue * 0.97).toFixed(2);
            const cardReducedVal = (cardValue * 0.97).toFixed(2);

            // Difference (what restaurant keeps)
            const cashDiffVal = (cashValue * 0.03).toFixed(2);
            const cardDiffVal = (cardValue * 0.03).toFixed(2);

            // Update comparison fields
            cashOriginal.textContent = '$' + cashValue.toFixed(2);
            cashReduced.textContent = '  $' + cashReducedVal;
            cashDifference.textContent = '$' + cashDiffVal;

            cardOriginal.textContent = '$' + cardValue.toFixed(2);
            cardReduced.textContent = '  $' + cardReducedVal;
            cardDifference.textContent = '$' + cardDiffVal;

            // Show comparison
            cashComparison.classList.remove('d-none');
            cardComparison.classList.remove('d-none');

        } else {
            toggleStatus.innerHTML = '3% deduction is <strong>NOT</strong> applied.';
            // Hide comparison
            cashComparison.classList.add('d-none');
            cardComparison.classList.add('d-none');
        }

        // After changing the toggle, try redistributing immediately
        performDistribution();
    });
});
