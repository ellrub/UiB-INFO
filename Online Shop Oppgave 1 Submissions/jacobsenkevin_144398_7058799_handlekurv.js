const varer = [
    {navn: "Datamaskin", pris: "30000"},
    {navn: "Mobiltelefon", pris: "60000"},
    {navn: "Gaming skjerm", pris: "15000"},
    {navn: "Datamus", pris: "5000"},
    {navn: "Fidget spinner", pris: "3000"},
    {navn: "Krusedull av Scamotronics© eier", pris: "1270851"},
    {navn: "Artig flosshatt", pris:"53123"},
    {navn:"Island sin siste McDonalds meny", pris:"4985340"}
];
let handlekurv = [];

const knapper = document.querySelectorAll(".kjøp-knapp");
if (knapper.length > 0) {
    knapper.forEach(knapp => {
        knapp.addEventListener("click", () => {
            const vareID = knapp.id;

                if (!handlekurv.includes(vareID)) {
                    handlekurv.push(vareID);
                }
                
                else {
                    alert("Forsøk på å kjøpe mer enn en vare. Forsøk blokkert.")
                    knapp.disabled = true;
                }
            });
        });
    }