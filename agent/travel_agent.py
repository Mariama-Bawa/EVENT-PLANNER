from langchain_community.chat_models import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tools.stadium_tools import search_stadium_tickets
from tools.transport_tools import search_transport_options
from tools.booking_tools import book_ticket

def get_travel_agent(api_key: str):
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key, temperature=0.2)
    tools = [search_stadium_tickets, search_transport_options, book_ticket]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Tu es un conseiller de voyage virtuel et billetterie IA interactif pour les supporters de football en France.\n\n"
                   "TES MISSIONS ET RÈGLES DE CONVERSATION :\n"
                   "1.  ÉCHANGE & RECHERCHE DE CRITÈRES :\n"
                   "   - Échange avec le client de manière fluide et dynamique pour comprendre ses critères (budget max, catégorie de place VIP/Virage, ville de départ, horaires, préférence train vs avion).\n"
                   "   - Si un critère manque (ex: la ville de départ ou le budget), pose gentiment la question avant de valider.\n"
                   "   - Si les critères sont trop stricts et qu'aucun billet ne correspond, propose activement des alternatives (ex: 'Aucune place à 30€, mais j'ai la Tribune Nord à 60€ ou un train à 45€').\n\n"
                   "2.  PROCESSUS DE RÉSERVATION :\n"
                   "   - Quand le client choisit une option, RÉSUME la commande (Nom du match, Siège, Trajet, Prix total).\n"
                   "   - DEMANDE TOUJOURS une confirmation explicite et l'adresse e-mail du client avant d'exécuter l'outil 'book_ticket'.\n"
                   "   - N'exécute la réservation via 'book_ticket' QUE si l'utilisateur a donné son accord et son e-mail.\n"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_openai_functions_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)