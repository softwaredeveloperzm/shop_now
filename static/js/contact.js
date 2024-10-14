
    const parentCookieName = "sessionData";

    function validateForm() {
        let valid = true;

        // Clear previous error messages
        document.getElementById('name-error').textContent = '';
        document.getElementById('email-error').textContent = '';

        // Get form values
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        // Validate name
        if (name === "") {
            document.getElementById('name-error').textContent = 'Name must be filled out';
            valid = false;
        }

        // Validate email
        if (email === "") {
            document.getElementById('email-error').textContent = 'Email must be filled out';
            valid = false;
        } else {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                document.getElementById('email-error').textContent = 'Invalid email format';
                valid = false;
            }
        }

        return valid;
    }

    function handleFormSubmit() {
        if (validateForm()) {
            storeFormDataAsCookies();
            logStoredData();
            showPaypalButton();
            hideForm(); // Hide the form after successful submission
            return false; // Prevent form submission
        }
        return false; // Prevent form submission if validation fails
    }

    function storeFormDataAsCookies() {
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        const data = {
            name: name,
            email: email
        };

        document.cookie = `${parentCookieName}=${encodeURIComponent(JSON.stringify(data))}; path=/`;
    }

    function getStoredData() {
        const cookieArr = document.cookie.split("; ");
        for (let i = 0; i < cookieArr.length; i++) {
            const cookiePair = cookieArr[i].split("=");
            if (cookiePair[0] === parentCookieName) {
                return JSON.parse(decodeURIComponent(cookiePair[1]));
            }
        }
        return null;
    }

    function logStoredData() {
        const storedData = getStoredData();
        console.log("Stored Data: ", storedData);
    }

    function showPaypalButton() {
        document.getElementById('main').style.display = 'block';
    }

    function hideForm() {
        document.getElementById('form').style.display = 'none';
    }

    function prefillForm() {
        const storedData = getStoredData();
        if (storedData) {
            document.getElementById('name').value = storedData.name;
            document.getElementById('email').value = storedData.email;
        }
    }

    document.addEventListener('DOMContentLoaded', prefillForm);

