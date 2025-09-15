(function() {
    emailjs.init("5tf1M3gzGZCHd6IcB"); // Replace with your Email.js public key
})();

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            emailjs.sendForm('service_46md2zv', 'template_rrw7m2c', form)
                .then(function () {
                    alert('Message sent successfully!');
                    form.reset();
                }, function (error) {
                    console.error('Failed...', error);
                    alert('Failed to send message. Please try again later.');
                });
        });
    }
});