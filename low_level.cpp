#include <cpr/cpr.h>
#include <fstream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

#include <iostream>
#include <chrono>


class Minion {
    public:
        int identifier;
        Eigen::MatrixXf a;
        Eigen::VectorXd b;
        Eigen::VectorXd x;
        bool isInit

        void Task(string jsonText){
            nlohmann::json json = nlohmann::json::parse(jsonText);
            this->id = json["id"];
            this->a = json["a"];
            this->b = json["b"];
            this->x = json["x"];
            this->time = json["time"];
            this->size = json["size"];
        }

        public:
            Minion() : identifier(-1), isInit(false) {}

            bool init(const std::string& url) {
                cpr::Response response = cpr::Get(cpr::Url{"http://localhost:8000"});
                if (response.status_code != 200) {
                  std::cerr << "Failed : " << response.status_code << std::endl;
                  return false;
                }

                nlohmann::json jsonData = nlohmann::json::parse(response.text);
                identifier = jsonResponse["identifier"];
                int size = jsonResponse["size"];
                a.resize(size, size);
                b.resize(size);
                x.resize(size);

                for (int i = 0; i < size; ++i) {
                  for (int j = 0; j < size; ++j) {
                    a(i, j) = jsonResponse["a"][i][j];
                  }
                  b(i) = jsonResponse["b"][i];
                }

                return true;
            }

            // Méthode work() mise à jour
            void solve() {
                // Déclaration et initialisation des variables start et end
                auto start = std::chrono::high_resolution_clock::now();
                auto end = start;

                // Résolution de l'équation matricielle
                x = a.lu().solve(b);

                // Calcul de la durée écoulée
                end = std::chrono::high_resolution_clock::now();
                std::chrono::duration<double> elapsed = end - start;

                // Affichage du temps pris
                std::cout << "Time taken: " << elapsed.count() << " seconds\n";
            }



};

int main() {
  Minion minion;
  minion.solve()

  return 0;
}