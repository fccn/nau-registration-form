**Archived repository**! 

Its content have been integrated directly on [nau-openedx-extensions](https://github.com/fccn/nau-openedx-extensions).

# nau-registration-form
This custom registration form extension for Open edX adds required fields for nau registration process

## Installation
1. Install the module in the edx platform virtualenv: `pip install -e .`
2. Edit lms.env.json:
    1. Add a new line containing: `"REGISTRATION_EXTENSION_FORM": "form_extender.forms.NauExtendedForm",`
    2. Add a new line containing: `"ADDL_INSTALLED_APPS": ["form_extender"],`
    3. Ensure combined login registration is set: `"ENABLE_COMBINED_LOGIN_REGISTRATION": true,`
    4. Save and exit editor.
3. Run migrations with `paver update_db`
4. Restart the LMS.
