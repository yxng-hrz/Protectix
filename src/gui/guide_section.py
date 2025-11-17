from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QTabWidget,
    QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def guide_section_widget():
    widget = QWidget()
    layout = QVBoxLayout()

    # Titre principal
    title = QLabel("🛡️ Guide de sécurité informatique")
    title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
    layout.addWidget(title)

    # Créer des onglets pour organiser le contenu
    tab_widget = QTabWidget()
    tab_widget.setStyleSheet("""
        QTabWidget::pane {
            border: 1px solid #ddd;
            background-color: white;
            padding: 10px;
        }
        QTabBar::tab {
            padding: 8px 15px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: #3498db;
            color: white;
        }
    """)

    # Onglet 1: Bonnes pratiques essentielles
    essentials_tab = create_essentials_tab()
    tab_widget.addTab(essentials_tab, "📋 Essentiels")

    # Onglet 2: Protection Internet
    internet_tab = create_internet_tab()
    tab_widget.addTab(internet_tab, "🌐 Internet")

    # Onglet 3: En cas de problème
    emergency_tab = create_emergency_tab()
    tab_widget.addTab(emergency_tab, "🚨 Urgences")

    layout.addWidget(tab_widget)

    # Onglet 4: Protection avancée
    advanced_tab = create_advanced_tab()
    tab_widget.addTab(advanced_tab, "🔒 Avancé")

    widget.setLayout(layout)
    return widget


def create_essentials_tab():
    """Crée l'onglet des pratiques essentielles."""
    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setStyleSheet("font-family: Arial; font-size: 14px; line-height: 1.5;")
    
    content = """
<h2>🔐 Sécurité des mots de passe</h2>
<ul>
<li><b>Longueur minimale :</b> 12 caractères (idéalement 16+)</li>
<li><b>Complexité :</b> Majuscules + minuscules + chiffres + symboles</li>
<li><b>Unicité :</b> Un mot de passe différent pour chaque compte important</li>
<li><b>Gestionnaire recommandé :</b> KeePass, Bitwarden ou 1Password</li>
<li><b>Double authentification (2FA) :</b> Activez-la partout où c'est possible</li>
<li><b>À éviter :</b> Dates de naissance, noms communs, séquences simples (123456)</li>
</ul>

<h2>🔄 Mises à jour système</h2>
<ul>
<li><b>Windows/Mac/Linux :</b> Activez les mises à jour automatiques</li>
<li><b>Navigateurs :</b> Chrome, Firefox, Edge - toujours à jour</li>
<li><b>Antivirus :</b> Mises à jour quotidiennes des définitions</li>
<li><b>Applications :</b> Mettez à jour dès qu'une notification apparaît</li>
<li><b>Firmware :</b> Routeur, imprimante - vérifiez mensuellement</li>
<li><b>Plugins navigateur :</b> Flash, Java - désinstallez si possible</li>
<li><b>Drivers :</b> Graphique, réseau - sources officielles uniquement</li>
</ul>

<h2>💾 Sauvegardes régulières</h2>
<ul>
<li><b>Règle 3-2-1 :</b> 3 copies, 2 supports différents, 1 hors site</li>
<li><b>Fréquence :</b> Documents importants = hebdomadaire, photos = mensuel</li>
<li><b>Solutions cloud :</b> Google Drive, OneDrive, Dropbox (avec chiffrement)</li>
<li><b>Disque externe :</b> Déconnectez après sauvegarde (protection ransomware)</li>
<li><b>Test :</b> Vérifiez que vous pouvez restaurer vos fichiers</li>
<li><b>Versionning :</b> Gardez plusieurs versions des fichiers importants</li>
<li><b>Automatisation :</b> Planifiez vos sauvegardes pour ne pas oublier</li>
</ul>

<h2>🖥️ Sécurité au quotidien</h2>
<ul>
<li><b>Verrouillage PC :</b> Win+L (Windows) quand vous partez</li>
<li><b>Wi-Fi public :</b> Évitez ou utilisez un VPN</li>
<li><b>Téléchargements :</b> Sources officielles uniquement</li>
<li><b>USB inconnu :</b> Ne jamais brancher</li>
<li><b>Permissions admin :</b> Utilisez un compte standard au quotidien</li>
<li><b>Pare-feu :</b> Toujours activé avec règles strictes</li>
<li><b>Partage fichiers :</b> Désactivez si non nécessaire</li>
<li><b>Bureau propre :</b> Pas de post-it avec mots de passe</li>
</ul>

<h2>📱 Sécurité mobile</h2>
<ul>
<li><b>Code PIN :</b> 6 chiffres minimum ou biométrie</li>
<li><b>Applications :</b> Play Store / App Store uniquement</li>
<li><b>Permissions :</b> Refusez celles qui semblent excessives</li>
<li><b>Localisation :</b> Activez "Localiser mon appareil"</li>
<li><b>Wi-Fi/Bluetooth :</b> Désactivez si non utilisés</li>
<li><b>Mises à jour :</b> iOS/Android toujours à jour</li>
<li><b>Sauvegarde :</b> iCloud/Google automatique activée</li>
<li><b>Apps bancaires :</b> Déconnexion automatique activée</li>
</ul>
"""
    
    text_edit.setHtml(content)
    return text_edit


def create_advanced_tab():
    """Crée l'onglet de protection avancée."""
    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setStyleSheet("font-family: Arial; font-size: 14px; line-height: 1.5;")
    
    content = """
<h2>🛡️ Types de malwares</h2>
<ul>
<li><b>Virus :</b> Se réplique en infectant d'autres fichiers
  <ul>
  <li>Protection : Antivirus à jour + scan régulier</li>
  <li>Ne pas ouvrir pièces jointes douteuses</li>
  </ul>
</li>
<li><b>Ransomware :</b> Chiffre vos fichiers contre rançon
  <ul>
  <li>Protection : Sauvegardes hors ligne</li>
  <li>Désactiver macros Office par défaut</li>
  <li>Si infecté : NE PAS payer</li>
  </ul>
</li>
<li><b>Trojan :</b> Se fait passer pour un logiciel légitime
  <ul>
  <li>Protection : Télécharger depuis sources officielles</li>
  <li>Vérifier signatures numériques</li>
  </ul>
</li>
<li><b>Spyware :</b> Espionne vos activités
  <ul>
  <li>Signes : PC lent, popups, page d'accueil modifiée</li>
  <li>Protection : Anti-spyware (Malwarebytes)</li>
  </ul>
</li>
</ul>

<h2>🔐 Chiffrement des données</h2>
<ul>
<li><b>Disque dur complet :</b>
  <ul>
  <li>Windows : BitLocker (Pro/Enterprise)</li>
  <li>Mac : FileVault 2</li>
  <li>Linux : LUKS</li>
  <li>Multiplateforme : VeraCrypt</li>
  </ul>
</li>
<li><b>Fichiers individuels :</b>
  <ul>
  <li>7-Zip avec mot de passe AES-256</li>
  <li>Documents Office : protection intégrée</li>
  <li>PDFs : Adobe Acrobat ou alternatives</li>
  </ul>
</li>
<li><b>Communications :</b>
  <ul>
  <li>WhatsApp/Signal : chiffrement bout-en-bout</li>
  <li>Email : ProtonMail ou GPG</li>
  <li>Navigation : Tor Browser pour anonymat</li>
  </ul>
</li>
</ul>

<h2>🌐 VPN et anonymat</h2>
<ul>
<li><b>Quand utiliser un VPN :</b>
  <ul>
  <li>Wi-Fi public (obligatoire)</li>
  <li>Contourner censure géographique</li>
  <li>Protection vie privée FAI</li>
  <li>Télétravail sécurisé</li>
  </ul>
</li>
<li><b>Choisir un VPN :</b>
  <ul>
  <li>No-logs policy vérifiée</li>
  <li>Kill switch automatique</li>
  <li>Protocoles modernes (OpenVPN, WireGuard)</li>
  <li>Éviter VPN gratuits (revendent données)</li>
  </ul>
</li>
</ul>

<h2>🔍 Hygiène numérique</h2>
<ul>
<li><b>Nettoyage régulier :</b>
  <ul>
  <li>Désinstaller programmes inutilisés</li>
  <li>Nettoyer cookies/cache navigateur</li>
  <li>Vérifier programmes au démarrage</li>
  <li>Supprimer comptes en ligne abandonnés</li>
  </ul>
</li>
<li><b>Audit de sécurité personnel :</b>
  <ul>
  <li>Lister tous vos comptes en ligne</li>
  <li>Vérifier mots de passe dupliqués</li>
  <li>Activer 2FA partout possible</li>
  <li>Réviser autorisations apps mobiles</li>
  </ul>
</li>
</ul>

<h2>🏠 Sécurité réseau domestique</h2>
<ul>
<li><b>Routeur/Box :</b>
  <ul>
  <li>Changer mot de passe admin par défaut</li>
  <li>Firmware à jour</li>
  <li>WPA3 ou WPA2 minimum</li>
  <li>Désactiver WPS</li>
  <li>Réseau invité séparé</li>
  </ul>
</li>
<li><b>Objets connectés (IoT) :</b>
  <ul>
  <li>Réseau isolé si possible</li>
  <li>Mots de passe forts</li>
  <li>Désactiver fonctions inutiles</li>
  <li>Vérifier politique vie privée</li>
  </ul>
</li>
</ul>

<h2>📚 Ressources pour approfondir</h2>
<ul>
<li><b>Sites officiels :</b>
  <ul>
  <li>ANSSI.gouv.fr - Guides et bonnes pratiques</li>
  <li>Cybermalveillance.gouv.fr - Assistance</li>
  <li>CNIL.fr - Protection données personnelles</li>
  <li>HaveIBeenPwned.com - Vérifier fuites données</li>
  </ul>
</li>
<li><b>Formation continue :</b>
  <ul>
  <li>MOOC SecNumAcadémie (ANSSI)</li>
  <li>Podcasts sécurité (NoLimitSecu)</li>
  <li>Chaînes YouTube spécialisées</li>
  <li>Forums et communautés</li>
  </ul>
</li>
</ul>
"""
    
    text_edit.setHtml(content)
    return text_edit


def create_internet_tab():
    """Crée l'onglet de sécurité Internet."""
    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setStyleSheet("font-family: Arial; font-size: 14px; line-height: 1.5;")
    
    content = """
<h2>📧 Sécurité des emails</h2>
<ul>
<li><b>Phishing - Signaux d'alerte :</b>
  <ul>
  <li>Urgence artificielle ("Agissez sous 24h!")</li>
  <li>Fautes d'orthographe</li>
  <li>Adresse expéditeur suspecte</li>
  <li>Demande d'infos personnelles</li>
  <li>Pièces jointes inattendues (.exe, .zip)</li>
  </ul>
</li>
<li><b>Réflexes :</b>
  <ul>
  <li>Vérifiez l'adresse réelle de l'expéditeur</li>
  <li>Survolez les liens sans cliquer</li>
  <li>En cas de doute, contactez directement l'entreprise</li>
  <li>Signalez sur signal-spam.fr</li>
  </ul>
</li>
</ul>

<h2>🌐 Navigation web sécurisée</h2>
<ul>
<li><b>HTTPS obligatoire pour :</b>
  <ul>
  <li>Sites bancaires</li>
  <li>Achats en ligne</li>
  <li>Connexion email/réseaux sociaux</li>
  <li>Tout formulaire avec données personnelles</li>
  </ul>
</li>
<li><b>Extensions utiles :</b>
  <ul>
  <li>uBlock Origin (bloqueur publicités)</li>
  <li>HTTPS Everywhere</li>
  <li>Privacy Badger</li>
  </ul>
</li>
</ul>

<h2>💬 Réseaux sociaux</h2>
<ul>
<li><b>Paramètres de confidentialité :</b>
  <ul>
  <li>Profil visible "Amis uniquement"</li>
  <li>Désactivez l'indexation moteurs de recherche</li>
  <li>Vérifiez les apps autorisées</li>
  <li>Limitez les infos dans "À propos"</li>
  <li>Photos : attention aux métadonnées GPS</li>
  <li>Historique : nettoyez régulièrement</li>
  </ul>
</li>
<li><b>Sécurité :</b>
  <ul>
  <li>N'acceptez que les contacts connus</li>
  <li>Photo profil sans infos sensibles</li>
  <li>Pas de géolocalisation en temps réel</li>
  <li>Méfiez-vous des quiz/jeux (collecte données)</li>
  <li>Vérifiez tags avant publication</li>
  <li>Paramètres enfants : contrôle parental</li>
  </ul>
</li>
<li><b>Arnaques courantes :</b>
  <ul>
  <li>Faux profils (vérifiez photos inversées)</li>
  <li>Offres trop belles (voyages gratuits)</li>
  <li>Demandes d'argent urgentes</li>
  <li>Liens raccourcis suspects</li>
  </ul>
</li>
</ul>

<h2>🛒 Achats en ligne</h2>
<ul>
<li><b>Sites fiables :</b>
  <ul>
  <li>URL commence par https://</li>
  <li>Mentions légales présentes</li>
  <li>Avis clients vérifiables</li>
  <li>Contact facilement accessible</li>
  <li>Labels : Trusted Shops, Fevad</li>
  <li>Recherchez avis sur Trustpilot</li>
  </ul>
</li>
<li><b>Paiement sécurisé :</b>
  <ul>
  <li>PayPal ou carte bancaire (jamais virement)</li>
  <li>Carte virtuelle si disponible</li>
  <li>Relevés bancaires vérifiés régulièrement</li>
  <li>3D Secure activé</li>
  <li>Évitez enregistrer carte sur sites</li>
  <li>Email confirmation obligatoire</li>
  </ul>
</li>
<li><b>Après l'achat :</b>
  <ul>
  <li>Conservez preuves (captures, emails)</li>
  <li>Suivez livraison</li>
  <li>Délai rétractation : 14 jours</li>
  <li>PayPal : protection 180 jours</li>
  </ul>
</li>
</ul>

<h2>🎮 Gaming et sécurité</h2>
<ul>
<li><b>Comptes de jeu :</b>
  <ul>
  <li>2FA sur Steam, Epic, Battle.net</li>
  <li>Email dédié pour gaming</li>
  <li>Mots de passe uniques</li>
  </ul>
</li>
<li><b>Communication :</b>
  <ul>
  <li>Discord : serveurs privés préférables</li>
  <li>Pas d'infos personnelles en vocal</li>
  <li>Méfiez-vous des liens dans chat</li>
  </ul>
</li>
<li><b>Téléchargements :</b>
  <ul>
  <li>Mods : sources officielles seulement</li>
  <li>Cracks = malware garantis</li>
  <li>Cheats = risque ban + virus</li>
  </ul>
</li>
</ul>
"""
    
    text_edit.setHtml(content)
    return text_edit


def create_emergency_tab():
    """Crée l'onglet des procédures d'urgence."""
    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setStyleSheet("font-family: Arial; font-size: 14px; line-height: 1.5;")
    
    content = """
<h2>🦠 Si vous pensez être infecté</h2>
<ol>
<li><b>Déconnectez immédiatement :</b>
  <ul>
  <li>Wi-Fi / Ethernet (pour éviter la propagation)</li>
  <li>Disques externes (protection des sauvegardes)</li>
  </ul>
</li>
<li><b>Mode sans échec :</b>
  <ul>
  <li>Windows : F8 au démarrage</li>
  <li>Mac : Shift au démarrage</li>
  </ul>
</li>
<li><b>Scan antivirus complet</b></li>
<li><b>Si ransomware :</b> NE PAS payer, cherchez un décrypteur gratuit</li>
<li><b>Dernier recours :</b> Réinstallation système depuis sauvegarde</li>
</ol>

<h2>🔓 Compte piraté</h2>
<ol>
<li><b>Changez immédiatement le mot de passe</b></li>
<li><b>Activez la double authentification</b></li>
<li><b>Vérifiez :</b>
  <ul>
  <li>Activités récentes du compte</li>
  <li>Paramètres de récupération</li>
  <li>Applications autorisées</li>
  <li>Règles de transfert email</li>
  </ul>
</li>
<li><b>Prévenez vos contacts</b> (risque de phishing)</li>
<li><b>Changez les mots de passe</b> des comptes liés</li>
</ol>

<h2>💳 Fraude bancaire</h2>
<ol>
<li><b>Contactez votre banque immédiatement</b></li>
<li><b>Faites opposition sur la carte</b></li>
<li><b>Déposez plainte</b> (commissariat ou gendarmerie)</li>
<li><b>Conservez toutes les preuves</b> (emails, relevés, captures)</li>
<li><b>Surveillez vos comptes</b> pendant plusieurs mois</li>
</ol>

<h2>📞 Contacts utiles</h2>
<ul>
<li><b>Info Escroqueries :</b> 0 805 805 817</li>
<li><b>Cybermalveillance.gouv.fr :</b> Assistance et conseils</li>
<li><b>Signal-spam.fr :</b> Signalement spams et phishing</li>
<li><b>CNIL :</b> Plainte violation données personnelles</li>
<li><b>Opposition carte bancaire :</b> 0 892 705 705</li>
</ul>

<h2>⚠️ Prévention future</h2>
<ul>
<li>Activez les alertes SMS/email bancaires</li>
<li>Utilisez des mots de passe uniques</li>
<li>Sauvegardez régulièrement</li>
<li>Restez informé des nouvelles menaces</li>
<li>Formez votre entourage</li>
</ul>
"""
    
    text_edit.setHtml(content)
    return text_edit