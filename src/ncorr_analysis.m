% Script dedicated to NCORR data analysis (Young's Modulus)

% Initializing average areas for each specimen
images = [4:15; 4:15; 4:15; 4:15; 4:15];
image_info = ["test00001.csv", "test00002.csv", "test00003.csv", "test00001.csv", "test00005.csv"];
rows = [200:625; 1:15; 1:15; 1:15; 1:15];
cols = [275:425; 1:15; 1:15; 1:15; 1:15];






for i = 1:5
    % Load the data
    data = load(['./results/NCORR/',num2str(i),'/test',num2str(i),'.mat']);
    stress_data = readtable(['./results/Data/B',num2str(i),'_parsed','.csv'], 'NumHeaderLines', 1);
    image_data = readtable(['./Data/Image Data/',num2str(i),'/',image_info(i)], 'NumHeaderLines', 1);

    % Extract the relevant stresses
    for j = images(i,:)
        for k = length(image_data(1,:))
            if image_data(1,k) == j
                t = image_data(3,k);
                break;
            end
        end

        for k 

        stress(j) = stress_data(j,2);
    end

    strainsXX = (data.data_dic_save1.strains(i).plot_exx_cur_formatted);
    strainsXY = (data.data_dic_save1.strains(i).plot_exy_cur_formatted);
    strainsYY = (data.data_dic_save1.strains(i).plot_eyy_cur_formatted);
    


    exx = zeros(images(i,:));
    exy = zeros(images(i,:));
    eyy = zeros(images(i,:));

    for j = images(i,:)
        exx(j) = average(strainsXX, cols(i,:), rows(i,:));
        exy(j) = average(strainsXY, cols(i,:), rows(i,:));
        eyy(j) = average(strainsYY, cols(i,:), rows(i,:));
    end

    E = 0;
    fprintf('Youngs Modulus for test %d: %f\n', i, E);
end

function E = youngsModules(stress, strain)
    
    E = stress/strain;
end

function avg = average(data, row, cols)
    data = 0

    for i = rows
        for j = cols
            avg = avg + data(i,j);
        end
    end
    avg = avg/(length(rows)*length(cols));
end