{
    'name': 'School Management',
    'version': '1.0.0',
    'summary': 'Gérer les élèves, enseignants et cours',
    'description': """
Module de gestion d'école.
--------------------------------
- Gestion des élèves
- Gestion des enseignants
- Gestion des cours et classes
    """,
    'author': 'TRAORE AROUNA',
    'website': 'https://eroarta.com',
    'license': 'LGPL-3',
    'category': 'Education',

    'depends': [
        'base','mail','sale_management', 'website',
        # 'mail',  # décommente si ton module utilise la messagerie interne
    ],
    'data': [
        'views/student_view.xml',
        'views/classe_view.xml',
        'views/course_view.xml',
        'views/sale_order_view.xml',
        'views/rendez_vous.xml',
        'views/student_web_template.xml',
        # 'views/note_view.xml',
        'data/student_data.xml',
        'data/school.classe.csv',
        'reports/student_report.xml',
        'reports/student_list_report.xml',


        'security/ir.model.access.csv',
        'security/school_security.xml',
        'wizards/create_student.xml',
        'wizards/print_student_list.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 1,
}
