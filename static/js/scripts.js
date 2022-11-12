
$(document).ready(function () {
    

    var $element = $('.inputSlider');
    var $inputx = $("#monthValue")
    var totalResultValue = 0;
    var monthlyResultValue = 0;
    var loanResultValue = 0;
    $element
        .rangeslider({
            polyfill: false
        })
    for (let slider of document.querySelectorAll(".rangeslider__handle")) {
        slider.addEventListener("mouseenter", () => {
            $element.rangeslider({})
                .on('input', function () {
                    if (slider.parentElement.id === "js-rangeslider-0") {
                        if (this.id === "inputSlider-1") {
                            var month = parseInt(this.value)
                            document.querySelector("#monthValue").value = month
                        }
                    }
                    if (slider.parentElement.id === "js-rangeslider-1") {
                        if (this.id === "inputSlider-2") {
                            var loan = parseInt(this.value)
                            document.querySelector("#loanValue").value = loan
                        }
                    }
                    calculateResults()

                    function calculateResults(monthInput = document.querySelector("#monthValue").value, loanInput = document.querySelector("#loanValue").value, percentInput = document.querySelector("#percentValue").value) {
                        monthInput = parseInt(monthInput)
                        loanInput = parseInt(loanInput)
                        loanResultValue = 1.01;
                        totalResultValue = Math.floor(loanInput / monthInput) * loanResultValue;
                        totalResultValue= totalResultValue.toFixed(2)
                        updateUI()
                    }

                    function updateUI() {
                        document.querySelector("#percentValue").innerText = `${totalResultValue}`
                    }
                });
        })
    }

});