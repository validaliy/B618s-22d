function hucreSabitle(hucreAdi) {
    if (hucreAdi == "doram") {
        document.getElementById("bands").value = "20";
        document.getElementById("pci").value = "227";
        document.getElementById("dlfreq").value = "8060";
    }
    else if (hucreAdi == "kardesler") {
        document.getElementById("bands").value = "20";
        document.getElementById("pci").value = "174";
        document.getElementById("dlfreq").value = "8060";
    }
    else if (hucreAdi == "261") {
        document.getElementById("bands").value = "1";
        document.getElementById("pci").value = "261";
        document.getElementById("dlfreq").value = "21376";
    }
    else if (hucreAdi == "399") {
        document.getElementById("bands").value = "3";
        document.getElementById("pci").value = "399";
        document.getElementById("dlfreq").value = "18749";
    }
    else if (hucreAdi == "219") {
        document.getElementById("bands").value = "3";
        document.getElementById("pci").value = "219";
        document.getElementById("dlfreq").value = "18749";
    }
    else if (hucreAdi == "55") {
        document.getElementById("bands").value = "1";
        document.getElementById("pci").value = "55";
        document.getElementById("dlfreq").value = "21376";
    }
  }