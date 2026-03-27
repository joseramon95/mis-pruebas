const form = document.getElementById('contact-form');

if (form) {
    const nombreInput = document.getElementById('nombre');
    const emailInput = document.getElementById('email');
    const mensajeInput = document.getElementById('mensaje');
    
    const styles = document.createElement('style');
    styles.textContent = `
        .input-error {
            border-color: #ef4444 !important;
            animation: shake 0.5s ease-in-out;
        }
        
        .input-success {
            border-color: #10b981 !important;
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
        
        .error-message {
            color: #ef4444;
            font-size: 0.85rem;
            margin-top: -0.5rem;
            margin-bottom: 0.5rem;
            display: none;
        }
        
        .error-message.show {
            display: block;
        }
        
        .success-message {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 1rem;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        form button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        form button.loading::after {
            content: '';
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid white;
            border-top-color: transparent;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin-left: 8px;
            vertical-align: middle;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(styles);
    
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function showError(input, message) {
        input.classList.add('input-error');
        input.classList.remove('input-success');
        
        let errorMsg = input.parentElement.querySelector('.error-message');
        if (!errorMsg) {
            errorMsg = document.createElement('div');
            errorMsg.className = 'error-message';
            input.parentElement.insertBefore(errorMsg, input);
        }
        errorMsg.textContent = message;
        errorMsg.classList.add('show');
    }
    
    function showSuccess(input) {
        input.classList.remove('input-error');
        input.classList.add('input-success');
        
        const errorMsg = input.parentElement.querySelector('.error-message');
        if (errorMsg) {
            errorMsg.classList.remove('show');
        }
    }
    
    function clearValidation(input) {
        input.classList.remove('input-error', 'input-success');
        const errorMsg = input.parentElement.querySelector('.error-message');
        if (errorMsg) {
            errorMsg.classList.remove('show');
        }
    }
    
    nombreInput.addEventListener('input', () => clearValidation(nombreInput));
    emailInput.addEventListener('input', () => clearValidation(emailInput));
    mensajeInput.addEventListener('input', () => clearValidation(mensajeInput));
    
    nombreInput.addEventListener('blur', function() {
        if (this.value.trim().length > 0 && this.value.trim().length < 2) {
            showError(this, 'El nombre debe tener al menos 2 caracteres');
        } else if (this.value.trim().length >= 2) {
            showSuccess(this);
        }
    });
    
    emailInput.addEventListener('blur', function() {
        if (this.value.trim().length > 0 && !validateEmail(this.value)) {
            showError(this, 'Por favor, ingresa un email válido');
        } else if (validateEmail(this.value)) {
            showSuccess(this);
        }
    });
    
    mensajeInput.addEventListener('blur', function() {
        if (this.value.trim().length > 0 && this.value.trim().length < 10) {
            showError(this, 'El mensaje debe tener al menos 10 caracteres');
        } else if (this.value.trim().length >= 10) {
            showSuccess(this);
        }
    });
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        let isValid = true;
        const nombre = nombreInput.value.trim();
        const email = emailInput.value.trim();
        const mensaje = mensajeInput.value.trim();
        
        if (!nombre || nombre.length < 2) {
            showError(nombreInput, 'Por favor, ingresa tu nombre completo');
            isValid = false;
        }
        
        if (!email || !validateEmail(email)) {
            showError(emailInput, 'Por favor, ingresa un email válido');
            isValid = false;
        }
        
        if (!mensaje || mensaje.length < 10) {
            showError(mensajeInput, 'El mensaje debe tener al menos 10 caracteres');
            isValid = false;
        }
        
        if (isValid) {
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Enviando...';
            submitBtn.disabled = true;
            
            const formData = new FormData(form);
            
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    const successDiv = document.createElement('div');
                    successDiv.className = 'success-message';
                    successDiv.innerHTML = '<i class="fas fa-check-circle"></i> ¡Mensaje enviado exitosamente! Te contactaré pronto.';
                    form.insertBefore(successDiv, form.firstChild);
                    
                    form.reset();
                    document.querySelectorAll('.input-success').forEach(el => {
                        el.classList.remove('input-success');
                    });
                    
                    setTimeout(() => {
                        successDiv.remove();
                    }, 5000);
                } else {
                    throw new Error('Error en el envío');
                }
            })
            .catch(error => {
                alert('Hubo un error al enviar el mensaje. Por favor, intenta de nuevo o contáctame directamente por WhatsApp.');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        }
    });
}
