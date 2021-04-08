interface algorithm_props {
    name: String
    short_name: String
    type: String
    stepped_enabled: boolean
}

export const algorithms : {[key: string]: algorithm_props}= {
    greedy: {
        name: "Greedy (González 1985)",
        short_name: "Greedy",
        type: "approximation",
        stepped_enabled: true
    },
    greedy_reduce: {
        name: "Greedy (modified to optimise radii)",
        short_name: "Greedy Reduce",
        type: "approximation",
        stepped_enabled: true
    },
    colourful_bandyapadhyay_pseudo: {
        name: "O(1)-colourful (Pseudo 2-approximation, Bandyapadhyay et al. 2019)",
        short_name: "Pseudo O(1)-colourful",
        type: "approximation",
        stepped_enabled: true
    },
    colourful_bandyapadhyay: {
        name: "O(1)-colourful (17-approximation, Bandyapadhyay et al. 2019)",
        short_name: "O(1)-colourful",
        type: "approximation",
        stepped_enabled: true
    },
    pbs: {
        name: "PBS (Pullan 2008)",
        short_name: "PBS",
        type: "genetic",
        stepped_enabled: true
    },
    colourful_pbs: {
        name: "Colourful PBS",
        short_name: "Colourful PBS",
        type: "genetic",
        stepped_enabled: true
    },
    brute_force_k_center: {
        name: "Brute force K-Center",
        short_name: "Brute force K-Center",
        type: "exact",
        stepped_enabled: false
    },
    brute_force_colourful_k_center: {
        name: "Brute force Colourful K-Center",
        short_name: "Brute force Colourful K-Center",
        type: "exact",
        stepped_enabled: false
    }
}