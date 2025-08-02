# CryptoForge-Noman-AI-Developer

## CryptoForge Nomad Project Scope and AI Developer Role

## 1. Project Overview
The CryptoForge Nomad is a secure, portable Bitcoin node and hardware wallet device, designed to function like a modern smartphone (e.g., iPhone) with integrated air-gapped security, advanced transaction management, and full node capabilities. It combines features from the Coldcard Q (hardware security), Sparrow (wallet usability), and Bitcoin Knots (node enhancements) to enable sovereign Bitcoin control: receiving, broadcasting, storing, signing, and verifying transactions.

**Key Design Principles**:
- **Portability**: Pocket-sized (150mm x 75mm x 10mm, ~200g), rugged IP67-rated enclosure.
- **Security**: Hardware-enforced air-gapping, dual secure elements, open-source firmware, anti-tampering.
- **Usability**: Intuitive touchscreen UI with gestures, app ecosystem.
- **Autonomy**: 24+ hours battery life, global connectivity (cellular/satellite).
- **Scalability**: Supports full/pruned blockchain (up to 1TB internal storage).

**Ultimate Goal**: Develop a working prototype for manufacturing by a hardware/software company. Estimated timeline: 12-18 months (hardware prototyping: 6 months; software integration: 4 months; security auditing: 2 months; beta testing: 3-6 months). Budget: $5-10M for R&D.

## 2. Functional Requirements
### 2.1 Bitcoin Wallet Operations (Coldcard Q + Sparrow Inspired)
- Generate/store BIP-39 seeds (TRNG or dice rolls; min 99 rolls for entropy).
- Offline/air-gapped PSBT signing (BIP-174; QR/NFC export/import).
- Coin control: UTXO selection, labeling, RBF/CPFP.
- Multisig: Up to 15-of-15, with policies (spending limits, 2FA).
- Privacy: Tor routing, PayNyms (BIP-47), coinjoins, no address reuse.
- Transaction editor: Visual/hex editing before signing/broadcasting.
- Duress modes: Duress wallet, "brick me" PIN, BIP-39 passphrases.

### 2.2 Bitcoin Node Operations (Bitcoin Knots Inspired)
- Full validating node: Verify ~600GB blockchain (pruned to 10GB).
- Transaction verification: Consensus rules, mempool management.
- Broadcasting: P2P relay, Tor anonymization.
- Filtering: Spam filters, bloom filters, configurable policies (min fees, block limits).
- Expert controls: RPC interface, testnet support.
- Management: IBD acceleration (UTXO snapshots), rescans, MicroSD exports.

### 2.3 Core Capabilities
- **Receive**: Background sync, push alerts.
- **Broadcast**: Via 5G/WiFi/satellite/mesh.
- **Store**: Keys in secure elements; blockchain on SSD.
- **Sign**: Always offline; QR/NFC for PSBT.
- **Verify**: Merkle proofs, full chain validation.
- Additional: QR scanner, NFC, app ecosystem, encrypted backups (7z, XOR splitting).

## 3. Non-Functional Requirements
- **Performance**: Sync <24 hours; signing <5 seconds.
- **Reliability**: MTBF >100,000 hours; connectivity failover.
- **Compliance**: BIP/GDPR/FCC/CE standards; open-source code.
- **Cost**: Manufacturing <$300/unit; retail $500-700.
- **Environmental**: -10°C to 50°C operation; recyclable materials.

## 4. Hardware Specifications
### 4.1 Processor and Compute
- SoC: Custom ARM (e.g., Snapdragon 8 Gen 3 equiv.), with ECC/SHA-256 co-processor.
- CPU: Octa-core (3.0GHz high-perf, 1.8GHz efficiency).
- GPU: Integrated for UI/QR.
- RAM: 16GB LPDDR5.

### 4.2 Storage
- Internal: 1TB NVMe SSD.
- Secure: Dual elements (ATECC608B + STSAFE), tamper-detection.
- Expandable: Dual MicroSD (2TB each).

### 4.3 Display and Input
- Screen: 6.1" OLED (1080x2400, 120Hz), Gorilla Glass.
- Input: Touchscreen, haptics, fingerprint/face biometrics.
- Camera: 12MP rear for QR; front for 2FA.

### 4.4 Battery and Power
- Battery: 5,000mAh, USB-C/Qi charging.
- Life: 24-48 hours mixed use; low-power modes.
- Management: AI optimization, solar input.

### 4.5 Connectivity
- Wireless: 5G, WiFi 6E, Bluetooth 5.3, NFC, satellite (Iridium/Starlink).
- Wired: USB-C 3.2.
- Sensors: GPS, accelerometer, light/proximity.

### 4.6 Enclosure
- Materials: Aluminum/polycarbonate.
- Dimensions: 150x75x10mm, 200g.
- Ports: USB-C, MicroSD.

## 5. Software Architecture
- OS: Custom Linux (AOSP/Ubuntu Touch), SELinux/AppArmor.
- Firmware: Open-source, OTA updates.
- Node: Bitcoin Knots v26.x fork, optimized for mobile.
- Wallet: "Nomad Wallet" app (Sparrow UI + Coldcard security).
- Security: Key isolation, verified boot, audits.
- UI: iOS-like gestures, dashboard, transaction builder.

## 6. Development and Manufacturing Considerations
- **Prototyping Phases**:
  1. Breadboarding (RPi 5 POC).
  2. Custom PCB (TSMC/Foxconn).
  3. Software porting (Knots to ARM, Qt UI).
- **Testing**: Pen-testing, benchmarks, beta program.
- **Risks/Mitigations**: Blockchain growth (external SSD/prune); regulatory (no KYC); supply chain (diversify vendors).

## 7. AI Developer's Responsibilities
The AI Developer is an autonomous multi-agent system coordinating the project toward a prototype. It handles:
- **Continuous Research**: Web/X searches for latest Bitcoin protocols, hardware suppliers (e.g., "best secure elements 2025"), software updates.
- **Development**: Code writing/simulations (e.g., Bitcoin Knots fork in Python, CAD/PCB schematics via FreeCAD code).
- **Testing**: Simulations (e.g., transaction verification in regtest mode, SPICE circuit sims).
- **Organization**: Dependency graphs (e.g., "Hardware specs before software"), task breakdown, progress tracking.
- **Reporting**: Weekly summaries, milestone reports (e.g., "Phase 1 complete: RPi POC ready for human assembly").

## 8. AI Developer's Limitations and Directions for Impossible Tasks
The AI cannot perform physical or real-world actions. For these, it provides detailed directions:
- **Physical Hardware Assembly**: "Outsource to ProtoLabs or electronics engineer on Upwork; provide CAD files [link], specs [list], and assembly instructions [step-by-step]. Estimated cost: $500-2000 for prototype."
- **Real-World Testing**: "Hire lab like UL for battery/extreme condition tests; supply device and test plan [detailed protocol]. Use simulations (e.g., code for virtual battery drain) as proxy."
- **Manufacturing**: "Partner with Foxconn/TSMC; submit PCB designs [Gerber files], BOM [list components], and production specs. Scale to 10,000 units for <$300 cost."
- **Regulatory Compliance**: "Engage legal firm for FCC/CE certification; provide device specs and emissions data from simulations. AI can research requirements but not file."
- General Directive: Flag all such tasks with "Human Intervention Required: [action + directions + estimated cost/time]."

## 9. Next Steps and Integration
This document serves as the central knowledge base. Feed into AI frameworks (e.g., LangChain vector DB) for reference. Review weekly for updates.

Last Updated: August 01, 2025
