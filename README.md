
AI agentique (OLLAMA), Décembre 2025, projet indivuduel

I-Mise en contexte
Dans le cadre de ma formation en Ingénierie Data Science et Cloud Computing à l'ENSA Oujda qui nous a permis de suivre une formation avec monsieur Souissi sur "l'initiation à l'IA agentique", ce projet vise à développer un Agent IA conversationnel autonome appliqué au secteur du transport et de la billetterie événementielle en France.

Les plateformes traditionnelles obligent souvent les utilisateurs à naviguer sur plusieurs sites pour réserver séparément leurs billets de match et leurs trajets (train ou/et avion). Ce projet répond à cette problématique en centralisant l'expérience grâce à une interface intelligente capable de négocier les critères, proposer des alternatives adaptées au budget et finaliser les réservations de manière fluide.

II-Description du projet : MonEVENT-PLANNER
MonEVENT-PLANNER est un assistant virtuel intelligent basé sur une architecture agentique (LangGraph / LangChain et modèles LLM). Il agit comme un conseiller de voyage personnalisé qui gère de A à Z l'organisation d'un déplacement pour un événement sportif.

III-Fonctionnalités clés :
Recherche intelligente de billetterie : Filtrage des places de stades (PSG, OL, OM, etc.) par ville, date, catégorie (VIP, Tribune) et prix maximal.

Comparateur de transports : Recherche et comparaison simultanées des options de trajet (trains TGV/InOui, vols) depuis la ville de départ de l'utilisateur jusqu'à la destination de l'événement.

Négociation et recommandations proactives : Si une demande exacte n'est pas disponible ou dépasse le budget, l'agent propose automatiquement des alternatives crédibles.

Réservation multi-services automatisée : Mise à jour en temps réel des disponibilités et confirmation par e-mail après validation explicite de l'utilisateur.

IV-Fiche Technique (Tech Stack)
Langage : Python 3.10+

Framework IA : LangChain / LangGraph, OpenAI (GPT-4o)

Données (Mock Data) : Base JSON structurée (stadium_tickets.json, train_tickets.json, flight_tickets.json)

Gestion de version : Git 
