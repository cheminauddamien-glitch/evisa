#!/usr/bin/env python3
"""
Appends missing code (LABELS, getLang, init, showResult) to visa-search.js
after the COMBOS line.
"""

import os
import subprocess
import sys

JS_PATH = os.path.join(os.path.dirname(__file__), "www", "js", "visa-search.js")

MISSING_CODE = r"""
  // Labels per language
  var LABELS = {
    en: { nat: "YOUR NATIONALITY", dest: "DESTINATION COUNTRY", purpose: "PURPOSE OF TRAVEL", btn: "Find Visa Info", duration: "Maximum Stay", overstay: "Overstay Penalty", strategy: "Entry / Exit Strategy", requirements: "Key Requirements", details: "Full Visa Details", guide: "Expat Guide", tourism: "Tourism / Vacation", student: "Student / Study", work: "Work / Employment", retirement: "Retirement", digital_nomad: "Digital Nomad" },
    fr: { nat: "VOTRE NATIONALITE", dest: "PAYS DE DESTINATION", purpose: "MOTIF DU VOYAGE", btn: "Trouver les Infos Visa", duration: "Sejour Maximum", overstay: "Penalite de Depassement", strategy: "Strategie Entree / Sortie", requirements: "Conditions Requises", details: "Details Complets du Visa", guide: "Guide Expatriation", tourism: "Tourisme / Vacances", student: "Etudiant / Etudes", work: "Travail / Emploi", retirement: "Retraite", digital_nomad: "Nomade Numerique" },
    es: { nat: "SU NACIONALIDAD", dest: "PAIS DE DESTINO", purpose: "MOTIVO DEL VIAJE", btn: "Buscar Info de Visa", duration: "Estancia Maxima", overstay: "Penalizacion por Exceso", strategy: "Estrategia Entrada / Salida", requirements: "Requisitos Clave", details: "Detalles Completos del Visa", guide: "Guia Expatriacion", tourism: "Turismo / Vacaciones", student: "Estudiante / Estudios", work: "Trabajo / Empleo", retirement: "Jubilacion", digital_nomad: "Nomada Digital" },
    pt: { nat: "SUA NACIONALIDADE", dest: "PAIS DE DESTINO", purpose: "MOTIVO DA VIAGEM", btn: "Encontrar Info do Visto", duration: "Estadia Maxima", overstay: "Penalidade por Excesso", strategy: "Estrategia Entrada / Saida", requirements: "Requisitos Principais", details: "Detalhes Completos do Visto", guide: "Guia Expatriacao", tourism: "Turismo / Ferias", student: "Estudante / Estudos", work: "Trabalho / Emprego", retirement: "Aposentadoria", digital_nomad: "Nomade Digital" }
  };

  function getLang() {
    var path = window.location.pathname;
    var m = path.match(/^\/(fr|es|pt|zh|th|ru|ar|ja|ko)\//);
    return m ? m[1] : "en";
  }

  function init() {
    var container = document.getElementById("visa-search-container");
    if (!container) return;
    var lang = getLang();
    var L = LABELS[lang] || LABELS.en;

    var natOpts = '<option value="">-- Select --</option>';
    NATIONALITIES.forEach(function(n) {
      natOpts += '<option value="' + n.s + '">' + n.n + '</option>';
    });
    var destOpts = '<option value="">-- Select --</option>';
    DESTINATIONS.forEach(function(d) {
      destOpts += '<option value="' + d.s + '">' + d.n + '</option>';
    });
    var purposeOpts = '<option value="">-- Select --</option>';
    PURPOSES.forEach(function(p) {
      purposeOpts += '<option value="' + p.s + '">' + (L[p.s] || p.n) + '</option>';
    });

    container.innerHTML =
      '<div class="visa-search-form">' +
        '<div class="visa-search-field">' +
          '<label for="vs-nat">' + L.nat + '</label>' +
          '<select id="vs-nat">' + natOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field">' +
          '<label for="vs-dest">' + L.dest + '</label>' +
          '<select id="vs-dest">' + destOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field">' +
          '<label for="vs-purpose">' + L.purpose + '</label>' +
          '<select id="vs-purpose">' + purposeOpts + '</select>' +
        '</div>' +
        '<div class="visa-search-field visa-search-btn-wrap">' +
          '<button id="vs-btn" type="button" class="btn btn-primary">' + L.btn + ' &rarr;</button>' +
        '</div>' +
      '</div>' +
      '<div id="visa-result-panel" style="display:none;"></div>';

    document.getElementById("vs-btn").addEventListener("click", function() { showResult(lang); });
  }

  function showResult(lang) {
    var nat = document.getElementById("vs-nat").value;
    var dest = document.getElementById("vs-dest").value;
    var purpose = document.getElementById("vs-purpose").value;
    var panel = document.getElementById("visa-result-panel");
    var L = LABELS[lang] || LABELS.en;

    if (!nat || !dest || !purpose) {
      panel.style.display = "block";
      panel.innerHTML = '<div class="visa-result-error">Please select all three fields.</div>';
      return;
    }

    var countryData = D[dest];
    if (!countryData) {
      panel.style.display = "block";
      panel.innerHTML = '<div class="visa-result-error">No data available for this destination yet.</div>';
      return;
    }
    var info = countryData[purpose];
    if (!info) {
      panel.style.display = "block";
      panel.innerHTML = '<div class="visa-result-error">No data for this visa type in this country.</div>';
      return;
    }

    var destObj = DESTINATIONS.find(function(d) { return d.s === dest; });
    var destName = destObj ? destObj.n : dest;
    var destFlag = destObj ? destObj.f : "";

    var hasCombo = COMBOS[dest + "|" + nat];
    var visaLink = hasCombo
      ? "/" + lang + "/" + dest + "-visa-for-" + nat + "-citizens.html"
      : "/" + lang + "/visa-" + dest + ".html";

    var guideCountries = ["thailand","portugal","spain","mexico","vietnam","malaysia","japan","uae","colombia","panama","costa-rica","greece","georgia","paraguay","laos","cambodia"];
    var hasGuide = guideCountries.indexOf(dest) !== -1;
    var guideLink = "/" + lang + "/expat-guide-" + dest + ".html";

    var html =
      '<div class="visa-result-card">' +
        '<div class="visa-result-header">' +
          '<span class="fi fi-' + destFlag + '" style="font-size:28px;margin-right:12px;"></span>' +
          '<div>' +
            '<h3 style="margin:0;font-size:20px;color:#fff;">' + destName + ' \u2014 ' + info[0] + '</h3>' +
          '</div>' +
        '</div>' +
        '<div class="visa-result-body">' +
          '<div class="visa-result-grid">' +
            '<div class="visa-result-item">' +
              '<div class="visa-result-label">' + L.duration + '</div>' +
              '<div class="visa-result-value visa-result-duration">' + info[1] + '</div>' +
            '</div>' +
            '<div class="visa-result-item">' +
              '<div class="visa-result-label">' + L.overstay + '</div>' +
              '<div class="visa-result-value visa-result-overstay">' + info[2] + '</div>' +
            '</div>' +
          '</div>' +
          '<div class="visa-result-section">' +
            '<div class="visa-result-label">' + L.strategy + '</div>' +
            '<div class="visa-result-value">' + info[3] + '</div>' +
          '</div>' +
          '<div class="visa-result-section">' +
            '<div class="visa-result-label">' + L.requirements + '</div>' +
            '<div class="visa-result-value">' + info[4] + '</div>' +
          '</div>' +
          '<div class="visa-result-actions">' +
            '<a href="' + visaLink + '" class="btn btn-primary">' + L.details + ' &rarr;</a>' +
            (hasGuide ? '<a href="' + guideLink + '" class="btn btn-outline-light">' + L.guide + ' &rarr;</a>' : '') +
          '</div>' +
        '</div>' +
      '</div>';

    panel.style.display = "block";
    panel.innerHTML = html;
    panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
"""

def main():
    # 1. Read the file
    print(f"Reading {JS_PATH} ...")
    with open(JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 2. Check it currently ends with the COMBOS line (no closing IIFE)
    if "function showResult" in content:
        print("ERROR: showResult already exists in the file. Nothing to do.")
        sys.exit(1)

    if "var COMBOS" not in content:
        print("ERROR: Could not find 'var COMBOS' in the file. Aborting.")
        sys.exit(1)

    # 3. Append the missing code
    print("Appending missing code (LABELS, getLang, init, showResult) ...")
    with open(JS_PATH, "a", encoding="utf-8") as f:
        f.write(MISSING_CODE)

    print("File updated successfully.")

    # 4. Verify syntax with node -c
    print("Running syntax check: node -c ...")
    result = subprocess.run(
        ["node", "-c", JS_PATH],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("Syntax OK!")
    else:
        print("Syntax check FAILED:")
        print(result.stderr)
        sys.exit(1)

    print("Done.")

if __name__ == "__main__":
    main()
