from agent.travel_agent import get_travel_agent

def main():
    agent_executor = get_travel_agent()
    chat_history = ""

    print("=========================================================")
    print("---     MonEVENT-PLANNER : Billetterie & Voyage IA     ---")
    print("---  Dites moi le match au quel vous voulez assister   ---")
    print("---     Tapez 'quitter' pour fermer le programme."     ---)
    print("=========================================================\n")

    while True:
        try:
            user_input = input("Vous : ")
            
            if user_input.lower().strip() in ["quitter", "exit", "quit"]:
                print("\nAu revoir !")
                break

            if not user_input.strip():
                continue

            response = agent_executor.invoke({
                "input": user_input,
                "chat_history": chat_history
            })
            
            bot_reply = response['output']
            print(f"\nConseiller : {bot_reply}\n")
            
            # Mise à jour de l'historique
            chat_history += f"User: {user_input}\nAssistant: {bot_reply}\n"

        except Exception as e:
            print(f"\nUne erreur est survenue : {e}\n")

if __name__ == "__main__":
    main()