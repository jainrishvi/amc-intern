import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

# Fully Revamped Corporate Visual Interface with High-Fidelity Vector Brand Logo Typography
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risk Analytics - Tata Mutual Fund Style Guide</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style>
        :root {
            --tata-blue: #005A9C;
            --tata-green: #00A859;
        }
        /* Top-Down Vertical Branched Layout Architecture */
        .tree-container { display: flex; flex-direction: column; align-items: center; width: 100%; min-width: max-content; padding: 20px 0; }
        
        .node-box { background: #ffffff; border: 1px solid #cbd5e1; padding: 12px 14px; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); position: relative; z-index: 10; transition: all 0.2s ease-in-out; }
        .node-split { border-top: 4px solid var(--tata-blue); }
        
        /* Dynamic Shape Class Rule Selectors */
        .shape-rectangle { border-radius: 0px; }
        .shape-rounded { border-radius: 12px; }
        .shape-pill { border-radius: 9999px; padding: 16px 24px; }
        .shape-circle { border-radius: 50%; aspect-ratio: 1 / 1; display: flex; flex-direction: column; justify-content: center; align-items: center; min-width: 200px; max-width: 200px; }
        .shape-diamond { transform: rotate(0deg); border-radius: 8px; }
        
        /* Dynamic Leaf Colors */
        .leaf-green { border-top: 4px solid #10b981; background-color: #f0fdf4; }
        .leaf-red { border-top: 4px solid #ef4444; background-color: #fef2f2; }
        
        /* Vertical Flow Branch Connectors */
        .branch-wrapper { display: flex; gap: 48px; justify-content: center; position: relative; width: 100%; }
        .branch-column { display: flex; flex-direction: column; align-items: center; position: relative; }
        
        /* Straight Down Connector Bars */
        .vertical-drop-line { height: 24px; width: 2px; background-color: #cbd5e1; }
        
        /* Top Horizontal Splitting Wings */
        .branch-wing-left, .branch-wing-right { position: absolute; top: 0; height: 16px; border-top: 2px solid #cbd5e1; width: 50%; }
        .branch-wing-left { right: 50%; border-left: 2px solid #cbd5e1; border-top-left-radius: 8px; }
        .branch-wing-right { left: 50%; border-right: 2px solid #cbd5e1; border-top-right-radius: 8px; }
        
        /* Text Condition Labels over branches */
        .branch-label { font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 9999px; position: absolute; top: -12px; z-index: 20; transform: translateX(-50%); left: 50%; }
        
        .matrix-cell { text-align: center; padding: 16px; font-weight: bold; font-size: 1.25rem; border: 1px solid #e2e8f0; }

        .tata-kpi-gradient {
            background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans min-h-screen p-4 sm:p-8">

    <div class="max-w-7xl mx-auto bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-200">
        
        <div class="flex flex-col md:flex-row items-center justify-between border-b border-slate-100 p-6 sm:px-8 gap-4">
            
            <div class="text-center md:text-left order-2 md:order-1">
                <h1 class="text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-[#1A5296] to-[#249454] mb-1">🌳 Risk Analytics & Decision Studio</h1>
                <p class="text-sm text-slate-500 font-medium">Internal Data Analytics Workspace — Asset Management Modeling Engine</p>
            </div>

            <div class="bg-white px-6 py-3.5 rounded-xl border border-slate-100 shadow-2xs flex flex-col justify-center min-w-[210px] order-1 md:order-2">
                <div class="flex flex-col">
                    <svg viewBox="0 0 160 38" class="h-8 w-auto overflow-visible select-none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0 4.5h23.6V10H14.6v27.2H8.9V10H0V4.5z" fill="#1A5296"/>
                        <path d="M37.3 4.5h6.3l11.4 32.7h-5.9l-2.9-8.8H34.8l-2.9 8.8h-5.9L37.3 4.5zm5.7 19.3l-4.1-12.4-4.1 12.4h8.2z" fill="#1A5296"/>
                        <path d="M57.4 4.5H81V10H72V37.2h-5.7V10h-8.9V4.5z" fill="#1A5296"/>
                        <path d="M94.7 4.5H101l11.4 32.7h-5.9l-2.9-8.8H92.2l-2.9 8.8h-5.9L94.7 4.5zm5.7 19.3l-4.1-12.4-4.1 12.4h8.2z" fill="#1A5296"/>
                    </svg>
                    
                    <svg viewBox="0 0 160 22" class="h-[18px] w-auto overflow-visible mt-1.5 select-none" xmlns="http://www.w3.org/2000/svg">
                        <text x="0" y="17" font-family="'Segoe UI', 'Ubuntu', 'Calibri', sans-serif" font-size="19" font-weight="500" fill="#249454" letter-spacing="-0.3">mutual</text>
                        <text x="69" y="17" font-family="'Segoe UI', 'Ubuntu', 'Calibri', sans-serif" font-size="19" font-weight="500" fill="#1A5296" letter-spacing="-0.3">fund</text>
                    </svg>
                </div>
            </div>
        </div>

        <div class="p-6 sm:p-8 space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="p-6 bg-slate-50 rounded-xl border border-slate-200 hover:border-[#005A9C]/50 transition-all">
                    <h2 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2"><span class="text-[#005A9C]">🔹</span> 1. Select Dataset</h2>
                    <input type="file" id="csv-file" accept=".csv" class="block w-full text-sm text-slate-550 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-[#005A9C] file:text-white hover:file:bg-[#00467A] cursor-pointer shadow-xs"/>
                </div>

                <div id="step-prep" class="p-6 bg-slate-50 rounded-xl border border-slate-200 opacity-50 transition-all">
                    <h2 class="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2"><span class="text-[#00A859]">🔹</span> 2. Auto Variable Prep</h2>
                    <div class="space-y-2 text-sm text-slate-600 mb-4">
                        <div><span class="font-bold text-slate-700">🔢 Continuous/Numerical:</span> <span id="num-cols" class="font-mono bg-white px-2 py-0.5 border border-slate-200 rounded text-slate-800 font-semibold">-</span></div>
                        <div><span class="font-bold text-slate-700">🔤 Categorical:</span> <span id="cat-cols" class="font-mono bg-white px-2 py-0.5 border border-slate-200 rounded text-slate-800 font-semibold">-</span></div>
                    </div>
                    <button id="cap-btn" disabled class="mt-4 w-full bg-[#00A859] text-white font-bold py-2 px-4 rounded-lg cursor-not-allowed hover:bg-[#008F4A] transition-all shadow-sm opacity-50">
                        Cap Outliers (Keep Head 2.5% & Tail 2.5%)
                    </button>
                </div>
            </div>

            <div id="step-config" class="p-6 bg-slate-50 rounded-xl border border-slate-200 opacity-50 transition-all">
                <h2 class="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2"><span class="text-[#005A9C]">🔹</span> 3. Model Customization & Shapes</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Target Variable / Prediction Goal (Y)</label>
                        <select id="target-select" disabled class="w-full bg-white border border-slate-300 rounded-lg p-2.5 text-slate-800 focus:outline-none focus:border-[#005A9C] shadow-xs"></select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Select Predictor Variables (X)</label>
                        <div id="features-box" class="bg-white border border-slate-300 rounded-lg p-3 max-h-40 overflow-y-auto space-y-2 shadow-inner"></div>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Custom Max Tree Depth: <span id="depth-lbl" class="text-[#005A9C] font-bold">3</span></label>
                        <input type="range" id="tree-depth" min="1" max="4" value="3" class="w-full accent-[#005A9C]">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-2">Custom Max Leaf Nodes: <span id="leaf-lbl" class="text-[#005A9C] font-bold">8</span></label>
                        <input type="range" id="leaf-nodes" min="2" max="16" value="8" class="w-full accent-[#005A9C]">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 border-t border-slate-200/60 pt-4">
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-1.5">Custom Root Node Shape</label>
                        <select id="root-shape-select" class="w-full bg-white border border-slate-300 rounded-lg p-2 text-sm text-slate-700 focus:outline-none focus:border-[#005A9C]">
                            <option value="shape-circle" selected>Circle (Default)</option>
                            <option value="shape-rounded">Rounded Card</option>
                            <option value="shape-rectangle">Rectangle</option>
                            <option value="shape-pill">Pill Shape</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-slate-700 mb-1.5">Custom Terminal Leaf Node Shape</label>
                        <select id="leaf-shape-select" class="w-full bg-white border border-slate-300 rounded-lg p-2 text-sm text-slate-700 focus:outline-none focus:border-[#005A9C]">
                            <option value="shape-diamond" selected>Diamond / Hexagon Card (Default)</option>
                            <option value="shape-rounded">Rounded Card</option>
                            <option value="shape-rectangle">Rectangle</option>
                            <option value="shape-pill">Pill Shape</option>
                        </select>
                    </div>
                </div>

                <button id="build-btn" disabled class="mt-6 w-full bg-[#005A9C] text-white font-bold py-3 px-6 rounded-xl shadow-md cursor-not-allowed transition-all text-lg opacity-50">
                    ⚡ Compile Constraints & Run Model Diagnostics
                </button>
            </div>

            <div id="tree-canvas" class="hidden space-y-8">
                
                <div class="tata-kpi-gradient grid grid-cols-1 lg:grid-cols-3 gap-6 p-6 rounded-xl border border-sky-100 shadow-sm">
                    <div class="flex flex-col gap-4 justify-center">
                        <h3 class="text-xl font-black text-[#005A9C] uppercase tracking-wide">📊 Model KPI Scoreboard</h3>
                        <div class="text-[11px] text-slate-500 font-medium">
                            Active Feature Scope: <span id="active-vars-display" class="font-semibold text-slate-700"></span>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-3 mt-1">
                            <div class="bg-white border border-sky-200/60 rounded-xl p-3 text-center shadow-xs">
                                <span class="text-[10px] font-bold text-blue-800 uppercase tracking-wider">Model Accuracy</span>
                                <div id="accuracy-score" class="text-2xl font-black text-[#005A9C] mt-1">00.00%</div>
                            </div>
                            <div class="bg-white border border-emerald-200/60 rounded-xl p-3 text-center shadow-xs">
                                <span class="text-[10px] font-bold text-emerald-800 uppercase tracking-wider">Model Gini Index</span>
                                <div id="gini-score" class="text-2xl font-black text-[#00A859] mt-1">0.00</div>
                            </div>
                        </div>

                        <div class="bg-white border-2 border-[#005A9C] rounded-xl p-3.5 shadow-sm">
                            <span class="text-[10px] font-bold text-[#005A9C] uppercase tracking-widest block mb-1">👑 Primary Root Split Attribute</span>
                            <div id="isolated-root-text" class="text-sm font-black text-slate-900 font-mono">None Selected</div>
                        </div>
                    </div>

                    <div class="bg-white border border-slate-200 rounded-xl p-4 lg:col-span-2 shadow-xs">
                        <h4 class="text-sm font-bold text-slate-700 mb-3 text-center uppercase tracking-wider">Confusion Matrix Matrix</h4>
                        <div class="grid grid-cols-3 gap-1 max-w-sm mx-auto text-xs">
                            <div></div>
                            <div id="lbl-pred-good" class="text-center font-bold text-slate-500">Predicted Good</div>
                            <div id="lbl-pred-bad" class="text-center font-bold text-slate-500">Predicted Bad</div>
                            
                            <div id="lbl-act-good" class="flex items-center font-bold text-slate-500">Actual Good</div>
                            <div id="cm-tp" class="matrix-cell bg-emerald-50 text-emerald-700 rounded shadow-xs">0</div>
                            <div id="cm-fn" class="matrix-cell bg-rose-50 text-rose-700 rounded shadow-xs">0</div>
                            
                            <div id="lbl-act-bad" class="flex items-center font-bold text-slate-500">Actual Bad</div>
                            <div id="cm-fp" class="matrix-cell bg-rose-50 text-rose-700 rounded shadow-xs">0</div>
                            <div id="cm-tn" class="matrix-cell bg-emerald-50 text-emerald-700 rounded shadow-xs">0</div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-white border border-slate-200 rounded-xl p-6 shadow-xs">
                    <div class="p-4 bg-emerald-50/60 border border-emerald-100 rounded-xl">
                        <h4 class="text-sm font-bold text-emerald-800 flex items-center gap-1.5 uppercase tracking-wider"><span>🟢</span> Good Rate Explanation</h4>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">The **Good Rate** represents the percentage of desired positive events contained within that isolated node segment relative to its total population.</p>
                    </div>
                    <div class="p-4 bg-amber-50/60 border border-amber-100 rounded-xl">
                        <h4 class="text-sm font-bold text-amber-800 flex items-center gap-1.5 uppercase tracking-wider"><span>🔴</span> Bad Rate Explanation</h4>
                        <p class="text-xs text-slate-600 mt-2 leading-relaxed">The **Bad Rate** represents the opposite profile risk segment fraction active inside that specific split pool.</p>
                    </div>
                </div>

                <div class="w-full p-6 bg-slate-50 border-2 border-dashed border-slate-300 rounded-xl overflow-x-auto">
                    <h3 class="text-lg font-bold text-slate-800 mb-6">🌳 Finalized Model Architecture Graphical Tree Map</h3>
                    <div class="w-full overflow-auto">
                        <div class="tree-container">
                            <div id="tree-visualization-root" class="w-full flex flex-col items-center"></div>
                        </div>
                    </div>
                </div>

                <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-xs space-y-4">
                    <div class="border-b border-slate-100 pb-3">
                        <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">📈 4. Integrated Model ROC Curve Evaluation</h3>
                        <p class="text-xs text-slate-400 mt-0.5">This curve displays the cumulative separating power of the complete compiled decision tree across all selected predictors simultaneously.</p>
                    </div>
                    
                    <div id="roc-chart-area" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                            <div class="md:col-span-2 flex justify-center bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <svg id="roc-svg" viewBox="0 0 400 400" class="w-full max-w-sm h-auto font-mono text-[9px] text-slate-400 overflow-visible"></svg>
                            </div>
                            <div class="bg-blue-50/50 border border-blue-100 rounded-xl p-5 flex flex-col justify-center text-center">
                                <span class="text-xs font-bold text-blue-800 uppercase tracking-wider">Model ROC-AUC Score</span>
                                <span id="roc-auc-value" class="text-4xl font-black text-[#005A9C] mt-2">0.500</span>
                                <p class="text-[11px] text-slate-500 mt-3 leading-relaxed">Reflects how cleanly your current ruleset layout segments your positive target classes across your entire sample data frame.</p>
                            </div>
                        </div>

                        <div class="bg-slate-50 border border-slate-200 rounded-xl p-5 text-sm text-slate-600 leading-relaxed space-y-3">
                            <h4 class="font-bold text-slate-800 text-base flex items-center gap-1.5">💡 Understanding Your Model ROC Chart</h4>
                            <p>When modeling portfolio risks, there is a constant tug-of-war between catching real events (<span class="font-bold text-emerald-700">True Positives</span>) and accidentally throwing false alerts (<span class="font-bold text-rose-600">False Positives</span>). The ROC Curve charts this exact relationship across every mathematical split option.</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs bg-white p-3.5 rounded-lg border border-slate-200">
                                <div>
                                    <span class="font-bold text-slate-700 block mb-0.5">📉 Reading the Track:</span>
                                    The dashed diagonal line shows pure coin-toss guesswork. The further your solid blue line arches away from it toward the top-left, the sharper your feature is.
                                </div>
                                <div>
                                    <span class="font-bold text-slate-700 block mb-0.5">🏆 The AUC Score Guide:</span>
                                    A score of <span class="font-semibold font-mono">0.500</span> means zero predictive separation skill, while scores landing north of <span class="font-semibold font-mono">0.800</span> or <span class="font-semibold font-mono">0.900</span> reflect elite model screening strengths.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="p-5 bg-emerald-50 border border-emerald-200 text-emerald-900 rounded-xl shadow-xs text-center font-medium flex items-center justify-center gap-2">
                    ✨ <b>Your dataset is ready for further analytics, thank you!</b> 🥰
                </div>

            </div>
        </div>
    </div>

    <script>
        let datasetParsed = [];
        let headers = [];
        let numericVars = [];
        let categoricalVars = [];
        let totalLeavesGenerated = 0;
        let runtimeTreeModel = [];

        document.getElementById('csv-file').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(evt) {
                const lines = evt.target.result.split('\n').map(l => l.trim()).filter(l => l.length > 0);
                headers = lines[0].split(',');
                
                datasetParsed = lines.slice(1).map(line => {
                    let values = line.split(',');
                    let obj = {};
                    headers.forEach((h, i) => {
                        let val = values[i];
                        obj[h] = (val !== undefined && !isNaN(val) && val !== "") ? parseFloat(val) : val;
                    });
                    return obj;
                });

                numericVars = []; categoricalVars = [];
                let sampleRow = datasetParsed[0];
                headers.forEach(h => {
                    if (typeof sampleRow[h] === 'number') { numericVars.push(h); } 
                    else { categoricalVars.push(h); }
                });

                document.getElementById('num-cols').innerText = numericVars.join(', ') || 'None';
                document.getElementById('cat-cols').innerText = categoricalVars.join(', ') || 'None';

                let targetSelect = document.getElementById('target-select');
                targetSelect.innerHTML = "";

                headers.forEach(header => {
                    targetSelect.innerHTML += `<option value="${header}">${header}</option>`;
                });

                let defaultIndex = 0;
                for (let i = 0; i < headers.length; i++) {
                    let opt = headers[i].toLowerCase();
                    if(['survival', 'survived', 'status', 'target'].includes(opt)) {
                        defaultIndex = i;
                        break;
                    }
                }
                targetSelect.selectedIndex = defaultIndex;
                
                syncPredictorCheckboxes();

                document.getElementById('step-prep').classList.remove('opacity-50');
                let capBtn = document.getElementById('cap-btn');
                capBtn.removeAttribute('disabled');
                capBtn.classList.remove('opacity-50', 'cursor-not-allowed');

                document.getElementById('step-config').classList.remove('opacity-50');
                targetSelect.removeAttribute('disabled');
                let buildBtn = document.getElementById('build-btn');
                buildBtn.removeAttribute('disabled');
                buildBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            };
            reader.readAsText(file);
        });

        document.getElementById('target-select').addEventListener('change', function() {
            syncPredictorCheckboxes();
        });

        function syncPredictorCheckboxes() {
            let targetSelect = document.getElementById('target-select');
            let featureBox = document.getElementById('features-box');
            if(!targetSelect.value) return;
            let currentTarget = targetSelect.value;
            featureBox.innerHTML = "";
            headers.forEach(header => {
                let isChecked = (header === currentTarget) ? '' : 'checked';
                featureBox.innerHTML += `
                    <label class="flex items-center gap-2 text-slate-700 text-sm font-medium">
                        <input type="checkbox" value="${header}" ${isChecked} data-field="${header}" class="rounded accent-[#005A9C]"> ${header}
                    </label>
                `;
            });
        }

        document.getElementById('tree-depth').addEventListener('input', (e) => { document.getElementById('depth-lbl').innerText = e.target.value; });
        document.getElementById('leaf-nodes').addEventListener('input', (e) => { document.getElementById('leaf-lbl').innerText = e.target.value; });

        document.getElementById('cap-btn').addEventListener('click', function() {
            numericVars.forEach(col => {
                let values = datasetParsed.map(r => r[col]).filter(v => typeof v === 'number').sort((a,b) => a-b);
                if (values.length === 0) return;
                let q25 = values[Math.floor(values.length * 0.025)];
                let q975 = values[Math.floor(values.length * 0.975)];
                datasetParsed.forEach(row => {
                    if (row[col] < q25) row[col] = q25;
                    if (row[col] > q975) row[col] = q975;
                });
            });
            this.innerText = "✓ 2.5% Outliers Capped Successfully";
            this.style.backgroundColor = "#008F4A";
        });

        document.getElementById('build-btn').addEventListener('click', function() {
            let target = document.getElementById('target-select').value;
            let maxDepth = parseInt(document.getElementById('tree-depth').value);
            let maxLeaves = parseInt(document.getElementById('leaf-nodes').value);
            let features = Array.from(document.querySelectorAll('#features-box input:checked')).map(c => c.value).filter(f => f !== target);
            let chosenRootShape = document.getElementById('root-shape-select').value;
            let chosenLeafShape = document.getElementById('leaf-shape-select').value;

            if(features.length === 0) {
                alert("Please select feature variables.");
                return;
            }

            // Dynamically identify the positive class for binary calculations
            let targetValues = datasetParsed.map(d => String(d[target]).trim());
            let uniqueTargets = [...new Set(targetValues)];
            let posClass = uniqueTargets[0];
            let goodKeys = ['1', 'true', 'survived', 'good', 'yes', 'default'];
            for (let val of uniqueTargets) {
                if (goodKeys.includes(val.toLowerCase())) {
                    posClass = val;
                    break;
                }
            }

            // Update UI Confusion Matrix labels dynamically
            document.getElementById('lbl-pred-good').innerText = `Predicted ${posClass}`;
            document.getElementById('lbl-pred-bad').innerText = `Predicted Other`;
            document.getElementById('lbl-act-good').innerText = `Actual ${posClass}`;
            document.getElementById('lbl-act-bad').innerText = `Actual Other`;

            let scopeDisplay = document.getElementById('active-vars-display');
            scopeDisplay.innerHTML = features.map(f => `<span class="variable-badge">${f}</span>`).join('');

            document.getElementById('tree-canvas').classList.remove('hidden');
            let container = document.getElementById('tree-visualization-root');
            container.innerHTML = "";
            totalLeavesGenerated = 0;
            runtimeTreeModel = [];

            // Gini Impurity calculation supporting multiclass datasets
            function calculateGini(data) {
                if (data.length === 0) return 0;
                let counts = {};
                data.forEach(d => {
                    let val = String(d[target]).trim();
                    counts[val] = (counts[val] || 0) + 1;
                });
                let sumSq = 0;
                for (let c in counts) {
                    let p = counts[c] / data.length;
                    sumSq += p * p;
                }
                return 1 - sumSq;
            }

            function calculateBestSplit(data, currentFeatures) {
                let bestGiniGain = -1;
                let bestFeature = currentFeatures[0];
                let bestSplitValue = 0;
                let bestIsNumeric = true;

                let parentGini = calculateGini(data);

                currentFeatures.forEach(feat => {
                    let values = data.map(d => d[feat]).filter(v => v !== undefined && v !== "");
                    if (values.length === 0) return;
                    let isNumeric = values.every(v => typeof v === 'number');

                    if (isNumeric) {
                        let uniqueVals = [...new Set(values)].sort((a,b) => a-b);
                        for (let i = 0; i < uniqueVals.length - 1; i++) {
                            let midpoint = (uniqueVals[i] + uniqueVals[i+1]) / 2;
                            let left = data.filter(d => d[feat] <= midpoint);
                            let right = data.filter(d => d[feat] > midpoint);

                            if (left.length === 0 || right.length === 0) continue;

                            let lGini = calculateGini(left);
                            let rGini = calculateGini(right);

                            let combinedGini = (left.length / data.length) * lGini + (right.length / data.length) * rGini;
                            let gain = parentGini - combinedGini;

                            if (gain > bestGiniGain) {
                                bestGiniGain = gain; bestFeature = feat; bestSplitValue = midpoint; bestIsNumeric = true;
                            }
                        }
                    } else {
                        let uniqueVals = [...new Set(values)];
                        uniqueVals.forEach(val => {
                            let left = data.filter(d => d[feat] === val);
                            let right = data.filter(d => d[feat] !== val);

                            if (left.length === 0 || right.length === 0) return;

                            let lGini = calculateGini(left);
                            let rGini = calculateGini(right);

                            let combinedGini = (left.length / data.length) * lGini + (right.length / data.length) * rGini;
                            let gain = parentGini - combinedGini;

                            if (gain > bestGiniGain) {
                                bestGiniGain = gain; bestFeature = feat; bestSplitValue = val; bestIsNumeric = false;
                            }
                        });
                    }
                });

                return { feature: bestFeature, split: bestSplitValue, isNumeric: bestIsNumeric };
            }

            function computeSegmentMetrics(data) {
                let total = data.length;
                if (total === 0) return { goodRate: "0.00%", badRate: "0.00%", accuracy: "0.00%", majority: "None", rawGoodPct: 0 };

                let targetValues = data.map(d => String(d[target]).trim());
                let counts = {};
                targetValues.forEach(v => counts[v] = (counts[v] || 0) + 1);

                let majorityClass = ""; let maxCount = -1;
                for (let key in counts) {
                    if (counts[key] > maxCount) { maxCount = counts[key]; majorityClass = key; }
                }

                let localAccuracy = ((maxCount / total) * 100).toFixed(2) + "%";
                let goodCount = 0;
                for (let key in counts) {
                    if (key.toLowerCase() === posClass.toLowerCase()) { goodCount += counts[key]; }
                }
                
                let badCount = total - goodCount;
                return { 
                    goodRate: ((goodCount / total) * 100).toFixed(2) + "%", 
                    badRate: ((badCount / total) * 100).toFixed(2) + "%", 
                    accuracy: localAccuracy, 
                    majority: majorityClass,
                    rawGoodPct: (goodCount / total)
                };
            }

            let rootRule = calculateBestSplit(datasetParsed, features);
            let rootSign = rootRule.isNumeric ? "&le;" : "==";
            let rootFormattedSplit = rootRule.isNumeric ? parseFloat(rootRule.split).toFixed(2) : rootRule.split;
            document.getElementById('isolated-root-text').innerHTML = `${rootRule.feature} ${rootSign} ${rootFormattedSplit}`;

            function growTreeStructure(data, depth, pathId) {
                let metrics = computeSegmentMetrics(data);
                let targetValues = data.map(d => String(d[target]));
                let uniqueTargets = [...new Set(targetValues)];

                if (uniqueTargets.length <= 1 || depth >= maxDepth || totalLeavesGenerated >= maxLeaves - 1 || data.length <= 5) {
                    totalLeavesGenerated++;
                    runtimeTreeModel.push({ type: 'leaf', path: pathId, prediction: metrics.majority, goodProbability: metrics.rawGoodPct });
                    
                    let leafColorClass = pathId.endsWith('L') ? 'leaf-green' : 'leaf-red';
                    
                    return `
                        <div class="branch-column">
                            <div class="node-box ${leafColorClass} ${chosenLeafShape}">
                                <div class="text-xs font-bold uppercase tracking-wider text-slate-500">🎯 Leaf Outcome</div>
                                <div class="text-base font-black text-slate-800 mt-1">${metrics.majority}</div>
                                <div class="text-[10px] text-slate-500 mt-2 border-t border-slate-200/60 pt-1.5 space-y-0.5">
                                    N: <b>${data.length}</b> | Acc: <b>${metrics.accuracy}</b><br>
                                    🟢 ${posClass}: <b>${metrics.goodRate}</b> | 🔴 Other: <b>${metrics.badRate}</b>
                                </div>
                            </div>
                        </div>`;
                }

                let rule = calculateBestSplit(data, features);
                let leftBranchData = [], rightBranchData = [], sign = "&le;";

                if (rule.isNumeric) {
                    leftBranchData = data.filter(d => d[rule.feature] <= rule.split);
                    rightBranchData = data.filter(d => d[rule.feature] > rule.split);
                    rule.split = parseFloat(rule.split).toFixed(2);
                } else {
                    sign = "==";
                    leftBranchData = data.filter(d => d[rule.feature] === rule.split);
                    rightBranchData = data.filter(d => d[rule.feature] !== rule.split);
                }

                if (leftBranchData.length === 0 || rightBranchData.length === 0) {
                    totalLeavesGenerated++;
                    runtimeTreeModel.push({ type: 'leaf', path: pathId, prediction: metrics.majority, goodProbability: metrics.rawGoodPct });
                    
                    let leafColorClass = pathId.endsWith('L') ? 'leaf-green' : 'leaf-red';
                    
                    return `
                        <div class="branch-column">
                            <div class="node-box ${leafColorClass} ${chosenLeafShape}">
                                <div class="text-base font-bold text-slate-800">${metrics.majority}</div>
                            </div>
                        </div>`;
                }

                runtimeTreeModel.push({ type: 'split', path: pathId, feature: rule.feature, split: rule.split, isNumeric: rule.isNumeric });
                let layoutShapeClass = (depth === 0) ? chosenRootShape : 'shape-rounded';

                let html = `
                    <div class="branch-column">
                        <div class="node-box node-split ${layoutShapeClass}">
                            <div class="text-xs font-bold uppercase tracking-wider text-[#005A9C]">🔍 Split Variable</div>
                            <div class="text-sm font-black text-slate-800 font-mono mt-1">${rule.feature} ${sign} ${rule.split}</div>
                            <div class="text-[10px] text-slate-400 mt-1">Pool N: ${data.length}</div>
                            <div class="text-[9px] text-slate-500 mt-1 flex justify-center gap-1.5 border-t border-slate-100 pt-1">
                                <span>🟢 ${posClass}: ${metrics.goodRate}</span> <span>🔴 Other: ${metrics.badRate}</span>
                            </div>
                        </div>
                        
                        <div class="vertical-drop-line"></div>
                        
                        <div class="branch-wrapper">
                            <div class="branch-column w-1/2">
                                <div class="branch-wing-left"></div>
                                <span class="branch-label bg-emerald-100 text-emerald-800 font-mono">TRUE</span>
                                <div class="h-4"></div>
                                ${growTreeStructure(leftBranchData, depth + 1, pathId + 'L')}
                            </div>
                            
                            <div class="branch-column w-1/2">
                                <div class="branch-wing-right"></div>
                                <span class="branch-label bg-amber-100 text-amber-800 font-mono">FALSE</span>
                                <div class="h-4"></div>
                                ${growTreeStructure(rightBranchData, depth + 1, pathId + 'R')}
                            </div>
                        </div>
                    </div>`;
                return html;
            }

            container.innerHTML = growTreeStructure(datasetParsed, 0, 'R');

            let tp = 0, tn = 0, fp = 0, fn = 0;
            let correctCount = 0;
            let modelPredictionRows = [];

            datasetParsed.forEach(row => {
                let currentPath = 'R';
                let safety = 0;
                while(safety < 30) {
                    let rule = runtimeTreeModel.find(node => node.path === currentPath);
                    if(!rule) break;
                    if(rule.type === 'leaf') {
                        let actualVal = String(row[target]).trim();
                        let predictedVal = String(rule.prediction).trim();
                        
                        if (actualVal === predictedVal) {
                            correctCount++;
                        }

                        let isActualGood = (actualVal.toLowerCase() === posClass.toLowerCase());
                        let isPredictedGood = (predictedVal.toLowerCase() === posClass.toLowerCase());

                        if (isActualGood && isPredictedGood) tp++;
                        else if (!isActualGood && !isPredictedGood) tn++;
                        else if (!isActualGood && isPredictedGood) fp++;
                        else if (isActualGood && !isPredictedGood) fn++;

                        modelPredictionRows.push({
                            score: rule.goodProbability,
                            trueClass: isActualGood ? 1 : 0
                        });
                        break;
                    } else {
                        if(rule.isNumeric) {
                            currentPath += (row[rule.feature] <= parseFloat(rule.split)) ? 'L' : 'R';
                        } else {
                            currentPath += (row[rule.feature] === rule.split) ? 'L' : 'R';
                        }
                    }
                    safety++;
                }
            });

            document.getElementById('cm-tp').innerText = tp;
            document.getElementById('cm-tn').innerText = tn;
            document.getElementById('cm-fp').innerText = fp;
            document.getElementById('cm-fn').innerText = fn;

            let calculatedAccuracy = ((correctCount / datasetParsed.length) * 100).toFixed(2);
            document.getElementById('accuracy-score').innerText = `${calculatedAccuracy}%`;
            
            let denominator = (tp + fn) * (tn + fp);
            let giniIndex = 0.00;
            if (denominator !== 0) {
                giniIndex = Math.abs((tp * tn) - (fp * fn)) / denominator;
            }
            document.getElementById('gini-score').innerText = giniIndex.toFixed(3);

            modelPredictionRows.sort((a, b) => b.score - a.score);

            let totalPositives = modelPredictionRows.filter(p => p.trueClass === 1).length;
            let totalNegatives = modelPredictionRows.length - totalPositives;

            if (totalPositives > 0 && totalNegatives > 0) {
                let svg = document.getElementById('roc-svg');
                let svgPoints = ["50,350"];
                let tpCount = 0, fpCount = 0;
                let aucSum = 0;

                modelPredictionRows.forEach(pair => {
                    if (pair.trueClass === 1) { tpCount++; } 
                    else { fpCount++; aucSum += tpCount; }

                    let posX = 50 + (fpCount / totalNegatives) * 300;
                    let posY = 350 - (tpCount / totalPositives) * 300;
                    svgPoints.push(`${posX.toFixed(1)},${posY.toFixed(1)}`);
                });

                let fullModelAuc = aucSum / (totalPositives * totalNegatives);
                document.getElementById('roc-auc-value').innerText = fullModelAuc.toFixed(3);

                svg.innerHTML = `
                    <line x1="50" y1="50" x2="350" y2="50" stroke="#f1f5f9" stroke-width="2"/>
                    <line x1="350" y1="50" x2="350" y2="350" stroke="#f1f5f9" stroke-width="2"/>
                    <line x1="50" y1="350" x2="350" y2="350" stroke="#cbd5e1" stroke-width="2"/>
                    <line x1="50" y1="50" x2="50" y2="350" stroke="#cbd5e1" stroke-width="2"/>
                    <line x1="50" y1="350" x2="350" y2="50" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
                    <polyline points="${svgPoints.join(' ')}" fill="none" stroke="#005A9C" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <text x="45" y="365" text-anchor="middle">0.0</text>
                    <text x="200" y="365" text-anchor="middle">False Positive Rate (FPR)</text>
                    <text x="350" y="365" text-anchor="middle">1.0</text>
                    <text x="35" y="355" text-anchor="end">0.0</text>
                    <text x="35" y="200" text-anchor="middle" transform="rotate(-90, 20, 200)">True Positive Rate (TPR)</text>
                    <text x="35" y="55" text-anchor="end">1.0</text>
                `;
            }
        });
    </script>
</body>
</html>"""

def start_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("🌍 Local server running at http://localhost:8080")
    webbrowser.open("http://localhost:8080/index.html")
    httpd.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=start_server, daemon=True).start()
    input("Press Enter to stop the metrics engine layout loop...\\n")
