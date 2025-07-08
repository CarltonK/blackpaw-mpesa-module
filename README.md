# 🇰🇪 Odoo M-Pesa Payment Integration (Daraja API)

This custom Odoo 17+ module provides native M-Pesa STK Push integration using Safaricom's Daraja API.

📆 Built with Pythonic Odoo best practices for clean extensibility and future-proofing.

#  🚀 Features
✅ Initiate STK Push payments from within Odoo


✅ Store and manage M-Pesa API credentials securely


✅ Toggle between sandbox and production environments


✅ Simple admin UI for configuration


🔐 Built-in model-level access control
🔜 (Coming Soon): C2B confirmation, validation endpoints, and auto-reconciliation

# 💠 Installation
Clone the module into your Odoo custom addons directory:

git clone https://github.com/CarltonK/blackpaw-mpesa-module.git

Restart the Odoo server:
```bash
./odoo-bin -u mpesa_payment_module -d your_db_name
```

Activate developer mode and install the module via the Apps menu.

# ⚙️ Configuration

Navigate to Settings > M-Pesa Configuration

Fill in your Safaricom Daraja credentials:

Consumer Key
Consumer Secret
Shortcode
Passkey

Choose environment:
Sandbox for testing
Production for live

# 🔐 Security
Credentials are stored in a secured mpesa.config model.
Access is limited to administrators by default.

No sensitive data is logged unless explicitly enabled.

# 📓 Resources
Safaricom Daraja Docs: https://developer.safaricom.co.ke/
Odoo 17 Developer Docs: https://www.odoo.com/documentation/17.0

# 🧪 Development
Activate your virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Enable live logging for API debugging:

```bash
./odoo-bin -d your_db_name --dev=all
```

# 🤝 Contributing
Pull requests are welcome. Please follow Odoo's module structure and include clear commit messages.

# 📄 License
This project is licensed under the MIT License.

# ✨ Author
Made with ❤️ in Kenya by Blackpaw Innovations
