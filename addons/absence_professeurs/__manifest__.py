{
    'name': 'Gestion des absences des professeurs',
    'version': '1.0',
    'summary': 'Gestion des absences des professeurs',
    'description': 'Module pour gérer les absences des professeurs',
    'author': 'Projet Académique',
    'category': 'Education',
    'depends': ['base'],
  'data': [
    'views/menu.xml',
    'views/professeur_views.xml',
    'views/absence_views.xml',
    'security/ir.model.access.csv',
],
    'application': True,
}
