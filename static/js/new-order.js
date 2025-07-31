document.addEventListener('DOMContentLoaded', function () {
  const completeInput = document.getElementById('auto-complete');
  const registerButton = document.getElementById('register-button');
  const orderForm = document.getElementById('order-form');

  registerButton.addEventListener('click', function() {
    completeInput.value = "False";
    orderForm.submit();
  });
});
