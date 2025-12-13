{{ name | escape | underline}}

.. automodule:: {{ fullname }}

{% block attributes %}
{%- if attributes %}
.. rubric:: {{ _('Module Attributes') }}

.. autosummary::
   :toctree:
{% for item in attributes %}
   {{ item.split('.')[-1] }} <{{ item }}>
{%- endfor %}
{% endif %}
{%- endblock %}

{%- block functions %}
{%- if functions %}
.. rubric:: {{ _('Functions') }}

.. autosummary::
   :toctree:
{% for item in functions %}
   {{ item.split('.')[-1] }} <{{ item }}>
{%- endfor %}
{% endif %}
{%- endblock %}

{%- block classes %}
{%- if classes %}
.. rubric:: {{ _('Classes') }}

.. autosummary::
   :toctree:
{% for item in classes %}
   {{ item.split('.')[-1] }} <{{ item }}>
{%- endfor %}
{% endif %}
{%- endblock %}

{%- block exceptions %}
{%- if exceptions %}
.. rubric:: {{ _('Exceptions') }}

.. autosummary::
   :toctree:
{% for item in exceptions %}
   {{ item.split('.')[-1] }} <{{ item }}>
{%- endfor %}
{% endif %}
{%- endblock %}

{%- block modules %}
{%- if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :recursive:
{% for item in modules %}
  {{ item.split('.')[-1] }} <{{ item }}>
{%- endfor %}
{% endif %}
{%- endblock %}
